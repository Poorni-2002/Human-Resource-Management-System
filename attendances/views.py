from django.shortcuts import render, get_object_or_404, redirect
from .models import Attendances
from .forms import AttendanceForm
from django.contrib import messages


def attendance_list(request):
    records = Attendances.objects.all()
    return render(request, 'attendances/list.html', {'records': records})

def attendance_create(request):
    form = AttendanceForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Attendance added successfully.")
        return redirect('attendances:attendances_list')
    return render(request, 'attendances/form.html', {'form': form})

def attendance_update(request, pk):
    record = get_object_or_404(Attendances, pk=pk)
    form = AttendanceForm(request.POST or None, instance=record)
    if form.is_valid():
        form.save()
        messages.success(request, "Attendance updated successfully.")
        return redirect('attendances:attendances_list')
    return render(request, 'attendances/form.html', {'form': form})

def attendance_delete(request, pk):
    record = get_object_or_404(Attendances, pk=pk)
    if request.method == 'POST':
        record.delete()
        messages.success(request, "Attendance deleted successfully.")
        return redirect('attendances:attendances_list')
    return render(request, 'attendances/delete_confirm.html', {'record': record})
