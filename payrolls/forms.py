# payrolls/forms.py

from django import forms

class PayrollMonthForm(forms.Form):
    month = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'month'}),
        label='Payroll Month',
        input_formats=['%Y-%m']  # IMPORTANT: HTML month picker submits in this format
    )
