from django.shortcuts import render, redirect, get_object_or_404
from .models import Performance
from employees.models import Employee
from django.contrib.auth.decorators import login_required

@login_required
def performance_list(request):
    performances = Performance.objects.all()
    return render(request, 'performance/list.html', {'performances': performances})

@login_required
def performance_create(request):
    employees = Employee.objects.all()
    if request.method == 'POST':
        employee_id = request.POST['employee']
        review_date = request.POST['review_date']
        score = request.POST['score']
        feedback = request.POST['feedback']
        employee = Employee.objects.get(id=employee_id)
        Performance.objects.create(employee=employee, review_date=review_date, score=score, feedback=feedback)
        return redirect('performance:performance_list')
    return render(request, 'performance/form.html', {'employees': employees})


@login_required
def performance_update(request, pk):
    performance = get_object_or_404(Performance, pk=pk)
    employees = Employee.objects.all()
    if request.method == 'POST':
        performance.employee = Employee.objects.get(id=request.POST['employee'])
        performance.review_date = request.POST['review_date']
        performance.score = request.POST['score']
        performance.feedback = request.POST['feedback']
        performance.save()
        return redirect('performance:performance_list')
    return render(request, 'performance/form.html', {'performance': performance, 'employees': employees})


@login_required
def performance_delete(request, pk):
    performance = get_object_or_404(Performance, pk=pk)
    performance.delete()
    return redirect('performance:performance_list')
