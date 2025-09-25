# leave/forms.py
from django import forms
from .models import Leave

class LeaveForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields = ['employee', 'leave_type', 'start_date', 'end_date', 'reason']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'min': ''}),  # min will be set by JS
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'min': ''}),
            'employee': forms.HiddenInput(),  # Still required for submission!
        }
