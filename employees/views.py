from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from designations.models import Designation
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib import messages


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Employee  # Make sure it's imported from the correct app


@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/list.html', {'employees': employees})


@login_required
def employee_create(request):
    designations = Designation.objects.all()
    users = User.objects.all()
    if request.method == 'POST':
            data = request.POST
            profile_pic = request.FILES.get('profile_picture')
                    # Debug print

            
            employee = Employee(
                user_id=data['user'],
                employee_number=data['employee_number'],
                designation_id=data['designation'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                date_of_birth=data['date_of_birth'],
                nic=data['nic'],
                civil_status=data['civil_status'],
                email=data['email'],
                phone=data['phone'],
                basic_salary=data['basic_salary'],
                allowances=data['allowances'],
                deductions=data['deductions'],
                profile_picture=profile_pic
            )
            employee.save()
            return redirect('employees:employee_list')
            messages.success(request, 'Employee created successfully!')
            return redirect('employees:employee_list')
       
    return render(request, 'employees/form.html', {'designations': designations,'users':users})
    messages.success(request, "Employee created successfully.")
    messages.error(request, "Failed to create employee.")



@login_required
def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    designations = Designation.objects.all()
    users = User.objects.all()
    
    if request.method == 'POST':
        employee.employee_number = request.POST['employee_number']
        employee.first_name = request.POST['first_name']
        employee.last_name = request.POST['last_name']
        employee.email = request.POST['email']
        employee.phone = request.POST['phone']
        employee.nic = request.POST['nic']
        employee.civil_status = request.POST['civil_status']
        employee.basic_salary = request.POST['basic_salary']
        employee.allowances = request.POST['allowances']
        employee.deductions = request.POST['deductions']
        employee.designation_id = request.POST['designation']
        employee.user_id = request.POST['user']

        # Handle profile picture update if provided
        if 'profile_picture' in request.FILES:
            employee.profile_picture = request.FILES['profile_picture']

        # Safely update date of birth
        dob = request.POST['date_of_birth']
        if dob:
            employee.date_of_birth = datetime.strptime(dob, "%Y-%m-%d").date()

        employee.save()
        messages.success(request, 'Employee updated successfully!')
        return redirect('employees:employee_list')

    return render(request, 'employees/form.html', {
        'employee': employee,
        'designations': designations,
        'users': users
    })


@login_required
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return redirect('employees:employee_list')
    messages.success(request, 'Employee deleted successfully!')
    return redirect('employees:employee_list')
    messages.success(request, "Employee deleted successfully.")

@login_required
def user_profile(request):
    employee = get_object_or_404(Employee, user=request.user)
    return render(request, 'employees/myProfile.html', {'employee': employee})
