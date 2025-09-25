from django.db import models
from employees.models import Employee

class Performance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    review_date = models.DateField()
    score = models.IntegerField()
    feedback = models.TextField()

    def __str__(self):
        return f"{self.employee.first_name} - {self.score}"
