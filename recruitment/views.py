from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Vacancy, Application
from .forms import ApplicationForm, VacancyForm
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError


# Public
def public_vacancy_list(request):
    vacancies = Vacancy.objects.filter(published=True)
    return render(request, 'recruitment/vacancy_list.html', {'vacancies': vacancies})

def vacancy_detail(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk, published=True)
    return render(request, 'recruitment/vacancy_detail.html', {'vacancy': vacancy})

def apply_vacancy(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk, published=True)
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.vacancy = vacancy
            application.save()
            messages.success(request, 'Application submitted!')
            return redirect('recruitment:vacancy_list')
        else:
            print(form.errors)  # 👈 Add this line to debug
    else:
        form = ApplicationForm()

    # ✅ INCLUDE form in context
    return render(request, 'recruitment/apply_form.html', {
        'vacancy': vacancy,
        'form': form,  # <-- THIS LINE was missing
    })


# Admin CRUD for Vacancies
@login_required
def vacancy_list_admin(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'recruitment/vacancy_list_admin.html', {'vacancies': vacancies})


@login_required
def vacancy_create(request):
    if request.method == 'POST':
        form = VacancyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recruitment:vacancy_list_admin')
    else:
        form = VacancyForm()
    return render(request, 'recruitment/vacancy_form.html', {'form': form})

@login_required
def vacancy_update(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    if request.method == 'POST':
        form = VacancyForm(request.POST, instance=vacancy)
        if form.is_valid():
            form.save()
            return redirect('recruitment:vacancy_list_admin')
    else:
        form = VacancyForm(instance=vacancy)
    return render(request, 'recruitment/vacancy_form.html', {'form': form})

@login_required
def vacancy_delete(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    vacancy.delete()
    return redirect('recruitment/vacancy_confirm_delete.html', {'vacancy': vacancy})

@login_required
def vacancy_confirm_delete(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    if request.method == "POST":
        vacancy.delete()
        return redirect('recruitment:vacancy_list_admin')  # or wherever you list vacancies
    return render(request, 'recruitment/vacancy_confirm_delete.html', {'vacancy': vacancy})

# Admin view Applications

@login_required
def application_list_admin(request):
    # Fetch all applications
    applications = Application.objects.select_related('vacancy').all()

    # Mark all unread applications as read
    Application.objects.filter(is_read=False).update(is_read=True)

    return render(request, 'recruitment/application_list_admin.html', {'applications': applications})

def generate_offer_letter_pdf(request, application_id):
    try:
        application = Application.objects.get(id=application_id)
    except Application.DoesNotExist:
        return HttpResponse("Application not found", status=404)

    template_path = 'recruitment/offer_letter_template.html'
    context = {'application': application}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="Offer_Letter_{application.full_name}.pdf"'

    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse("Error generating PDF", status=500)
    return response 

def update_application_status(request, pk, new_status):
    application = get_object_or_404(Application, pk=pk)
    if new_status in ['approved', 'rejected', 'pending']:
        application.status = new_status
        application.save()

    if new_status == "approved":
        subject = "Your Job Application Has Been Approved"
        message = f"Hi {application.full_name}, congratulations! Your application for {application.vacancy.title} has been approved."
    elif new_status == "rejected":
        subject = "Your Job Application Has Been Rejected"
        message = f"Hi {application.full_name}, we regret to inform you that your application for {application.vacancy.title} has been rejected."
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[application.email],
            fail_silently=False,
        )
        messages.success(request, "Email sent successfully.")
    except BadHeaderError:
        messages.error(request, "Invalid header.")
    except Exception as e:
        messages.error(request, f"Failed to send email: {str(e)}")

    return redirect('recruitment:application_list')

@login_required
def dashboard(request):
    unread_count = Application.objects.filter(is_read=False).count()
    print("Unread Count---------------------" ,unread_count)
    return render(request, 'dashboard.html', {'unread_count': unread_count})

