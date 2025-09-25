from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from employees.models import Employee
from designations.models import Designation
from leave.models import Leave
from django.contrib.auth import login
from django.contrib import messages
from .models import UserProfile
from django.shortcuts import render, get_object_or_404
from recruitment.models import Application

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            print("=====================================")
            login(request, user)
            role = user.userprofile.role
            if role == 'admin':
                print("admin")
                return redirect('dashboard')
            elif role == 'employee':
                print("Employee")
                return redirect('employee_dashboard')
        else:
            messages.error(request, 'Invalid login credentials')
    return render(request, 'accounts/login.html')





def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    total_employees = Employee.objects.count()
    total_designations = Designation.objects.count()
    today_attendances = 15
    today_leaves = Leave.objects.count()
    unread_count = Application.objects.filter(is_read=False).count()
    
    context = {
        'total_employees': total_employees,
        'total_designations': total_designations,
        'today_attendances': today_attendances,
        'today_leaves': today_leaves,
        'unread_count': unread_count
    }
    return render(request, 'dashboard.html', context)  # ✅ This is required






@login_required
def employee_dashboard(request):
    # Get the Employee profile connected to this user
    employee = get_object_or_404(Employee, user=request.user)

    # Filter leaves by this employee
    my_leaves = Leave.objects.filter(employee=employee).count()
    today = timezone.now().date()

    # Filter leaves that start or end in the current month
    current_month_leaves = Leave.objects.filter(
        employee=employee,
        start_date__month=today.month,
        start_date__year=today.year
    ).count()

    context = {
        'my_leaves': my_leaves,
        'current_month_leaves': current_month_leaves,
    }
    return render(request, 'employee_dashboard.html', context)
