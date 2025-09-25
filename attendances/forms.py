from django import forms
from .models import Attendances

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendances
        fields = ['employee', 'date', 'check_in', 'check_out', 'status']
        widgets = {
            'employee': forms.Select(attrs={'class': 'form-select'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'check_in': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'check_out': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }
