from django.db import models
from employees.models import Employee

class Leave(models.Model):
    LEAVE_TYPES = [
        ('Sick', 'Sick'),
        ('Casual', 'Casual'),
        ('Annual', 'Annual'),
        ('Maternity', 'Maternity'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=20, choices=LEAVE_TYPES)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()

    def __str__(self):
        return f"{self.employee} - {self.leave_type}"

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')