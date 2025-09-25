from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Report
from .forms import ReportForm
from django.template.loader import get_template
from xhtml2pdf import pisa

def report_list(request):
    reports = Report.objects.all()
    return render(request, 'reports/report_list.html', {'reports': reports})

def report_create(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('reports:report_list')
    else:
        form = ReportForm()
    return render(request, 'reports/report_form.html', {'form': form})

def report_update(request, pk):
    report = get_object_or_404(Report, pk=pk)
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES, instance=report)
        if form.is_valid():
            form.save()
            return redirect('reports:report_list')
    else:
        form = ReportForm(instance=report)
    return render(request, 'reports/report_form.html', {'form': form})

def report_download(request, pk):
    report = get_object_or_404(Report, pk=pk)
    if report.file:
        response = HttpResponse(report.file, content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename={report.file.name.split("/")[-1]}'
        return response
    return HttpResponse("No file found.")


def report_generate(request, pk):
    report = Report.objects.get(pk=pk)
    template = get_template('reports/report_pdf_template.html')
    html = template.render({'report': report})

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="report_{report.pk}.pdf"'

    pisa.CreatePDF(html, dest=response)
    return response
