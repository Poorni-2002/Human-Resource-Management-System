from django.db import models
from employees.models import Employee

class Attendances(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    check_in = models.TimeField()
    check_out = models.TimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('On Leave', 'On Leave')
    ])

    def __str__(self):
        return f"{self.employee} - {self.date} ({self.status})"
