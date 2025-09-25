from django.shortcuts import render, redirect, get_object_or_404
from .models import Leave
from .forms import LeaveForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from employees.models import Employee
from django.utils import timezone
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError

from django.conf import settings

@login_required
def leave_list(request):
    leaves = Leave.objects.all()
    return render(request, 'leave/leave_list.html', {'leaves': leaves})

@login_required



def leave_create(request):
    employee = Employee.objects.get(user=request.user)

    if request.method == 'POST':
        form = LeaveForm(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.employee = employee  # Link to logged-in employee
            leave.save()
            messages.success(request, "Leave request submitted successfully!")
            return redirect('leave:my_leaves')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = LeaveForm(initial={'employee': employee})  # Pre-fill hidden employee

    return render(request, 'leave/leave_form.html', {'form': form})


@login_required
def leave_update(request, pk):
    leave = get_object_or_404(Leave, pk=pk)

    if leave.status != 'pending':
        messages.error(request, "You can't edit a leave that has been approved or rejected.")
        return redirect('leave:leave_list')
    if request.method == 'POST':
        form = LeaveForm(request.POST, instance=leave)
        if form.is_valid():
            form.save()
            messages.success(request, "Leave request updated.")
            return redirect('leave:my_leaves')
    else:
        form = LeaveForm(instance=leave)
    return render(request, 'leave/leave_form.html', {'form': form})

@login_required
def leave_delete(request, pk):
    leave = get_object_or_404(Leave, pk=pk)

    if leave.status != 'pending':
        messages.error(request, "You can't delete a leave that has been approved or rejected.")
        return redirect('leave:leave_list')
    if request.method == 'POST':
        leave.delete()
        messages.success(request, "Leave request deleted.")
        return redirect('leave:my_leaves')
    return render(request, 'leave/leave_confirm_delete.html', {'leave': leave})

@login_required
def my_leaves(request):
    employee = Employee.objects.get(user=request.user)
    leaves = Leave.objects.filter(employee=employee)
    return render(request, 'leave/leave_list.html', {'leaves': leaves})

@login_required


def leave_approve(request, pk):
    leave = get_object_or_404(Leave, pk=pk)
    leave.status = 'Approved'
    leave.save()

    # Send email
    try:
        send_mail(
            subject='Leave Application Approved',
            message=f'Hi {leave.employee.first_name}, your leave from {leave.start_date} to {leave.end_date} has been approved.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[leave.employee.email],
            fail_silently=False,
        )
        messages.success(request, "Email sent successfully.")
    except BadHeaderError:
        messages.error(request, "Invalid header.")
    except Exception as e:
        messages.error(request, f"Failed to send email: {str(e)}")

    return redirect('leave:leave_list')


@login_required
def leave_reject(request, pk):
    leave = get_object_or_404(Leave, pk=pk)
    leave.status = 'Rejected'
    leave.save()

    try:
        send_mail(
            subject='Leave Application Rejected',
            message=f'Hi {leave.employee.first_name}, your leave from {leave.start_date} to {leave.end_date} has been rejected.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[leave.employee.email],
            fail_silently=False,
        )
        messages.success(request, "Email sent successfully.")
    except BadHeaderError:
        messages.error(request, "Invalid header.")
    except Exception as e:
        messages.error(request, f"Failed to send email: {str(e)}")

    return redirect('leave:leave_list')

