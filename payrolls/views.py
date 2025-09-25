from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.shortcuts import render, redirect
from employees.models import Employee

from .forms import PayrollMonthForm
from datetime import datetime
from django.shortcuts import render
from calendar import month_name
from .models import Payroll
from django.db.models import Q
from django.contrib.auth.decorators import login_required

@login_required
def create_monthly_payrolls(request):
    form = PayrollMonthForm()
    if request.method == 'POST':
        form = PayrollMonthForm(request.POST)
        if form.is_valid():
            print("============================================")
            month = form.cleaned_data['month']
            print("Generating payroll for month:", month)  # Debug print
            employees = Employee.objects.all()
            for emp in employees:
                basic = emp.basic_salary or 0
                allowances = emp.allowances or 0  # Replace with actual logic
                deductions = emp.deductions or 0   # Replace with actual logic
                net = basic + allowances - deductions

                Payroll.objects.update_or_create(
                    employee=emp,
                    month=month,
                    defaults={
                        'basic_salary': basic,
                        'total_allowances': allowances,
                        'total_deductions': deductions,
                        'net_salary': net
                    }
                )
            return redirect('payrolls:payroll_list')
        else:
            print("Form is invalid:", form.errors)  # Debug print
    return render(request, 'payrolls/create_monthly_payroll.html', {'form': form})





@login_required
def payroll_list(request):
    # Month dropdown list
    months = [(str(i), month_name[i]) for i in range(1, 13)]

    # Get filter input
    employee_name = request.GET.get('employee_name', '').strip()
    selected_month = request.GET.get('month', '').strip()
    selected_year = request.GET.get('year', '').strip()

    payrolls_qs = Payroll.objects.all()

    # Filter by first_name or last_name (case-insensitive)
    if employee_name:
        payrolls_qs = payrolls_qs.filter(
            Q(employee__first_name__icontains=employee_name) |
            Q(employee__last_name__icontains=employee_name)
        )

    # Filter by month number
    if selected_month:
        payrolls_qs = payrolls_qs.filter(month__month=int(selected_month))

    # Filter by year
    if selected_year:
        payrolls_qs = payrolls_qs.filter(month__year=int(selected_year))

    context = {
        'payrolls': payrolls_qs,
        'months': months,
        'selected_month': selected_month,
        'selected_year': selected_year,
        'employee_name': employee_name,
    }

    return render(request, 'payrolls/payroll_list.html', context)



@login_required
def export_payroll_pdf(request):
    employee_name = request.GET.get('employee_name', '').strip()
    month = request.GET.get('month', '')
    year = request.GET.get('year', '')

    payrolls = Payroll.objects.all()

    # If the user is an employee, restrict to their own records
    if request.user.userprofile.role == 'employee':
        payrolls = payrolls.filter(employee=request.user.employee)

    # Otherwise, filter by employee name if provided
    elif employee_name:
        payrolls = payrolls.filter(
            Q(employee__first_name__icontains=employee_name) |
            Q(employee__last_name__icontains=employee_name)
        )

    # Filter by month and year
    if month:
        payrolls = payrolls.filter(month__month=int(month))
    if year:
        payrolls = payrolls.filter(month__year=int(year))

    # Render to PDF
    template_path = 'payrolls/payroll_pdf_template.html'
    context = {
        'payrolls': payrolls,
        'selected_month': month,
        'selected_year': year,
        'employee_name': employee_name,
    }

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="payroll_report.pdf"'

    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('PDF generation failed')

    return response


@login_required
def my_payroll(request):
    employee = Employee.objects.get(user=request.user)
    payrolls_qs = Payroll.objects.filter(employee=employee)
     # Month dropdown list
    months = [(str(i), month_name[i]) for i in range(1, 13)]

    # Get filter input
    
    selected_month = request.GET.get('month', '').strip()
    selected_year = request.GET.get('year', '').strip()

    



    # Filter by month number
    if selected_month:
        payrolls_qs = payrolls_qs.filter(month__month=int(selected_month))

    # Filter by year
    if selected_year:
        payrolls_qs = payrolls_qs.filter(month__year=int(selected_year))

    context = {
        'payrolls': payrolls_qs,
        'months': months,
        'selected_month': selected_month,
        'selected_year': selected_year,
        
    }
    return render(request, 'payrolls/payroll_list.html',  context)