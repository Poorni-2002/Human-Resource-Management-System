from django.shortcuts import render, redirect, get_object_or_404
from .models import Designation
from django.contrib.auth.decorators import login_required

@login_required
def designation_list(request):
    designations = Designation.objects.all()
    return render(request, 'designations/list.html', {'designations': designations})

@login_required
def designation_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        Designation.objects.create(title=title, description=description)
        return redirect('designations:designation_list')
    return render(request, 'designations/form.html')

@login_required
def designation_update(request, pk):
    designation = get_object_or_404(Designation, pk=pk)
    if request.method == 'POST':
        designation.title = request.POST['title']
        designation.description = request.POST['description']
        designation.save()
        return redirect('designations:designation_list')
    return render(request, 'designations/form.html', {'designation': designation})

@login_required
def designation_delete(request, pk):
    designation = get_object_or_404(Designation, pk=pk)
    designation.delete()
    return redirect('designations:designation_list')
