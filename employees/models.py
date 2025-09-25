from django.db import models
from designations.models import Designation
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    employee_number = models.CharField(max_length=20, unique=True, default='TEMP001')
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    nic = models.CharField(max_length=20, blank=True)
    civil_status = models.CharField(max_length=20, choices=[
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed'),
    ], blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)
    allowances = models.DecimalField(max_digits=10, decimal_places=2)
    deductions = models.DecimalField(max_digits=10, decimal_places=2)

    profile_picture = models.ImageField(
    upload_to='profile_pictures/',
    default='profile_pictures/images_img.jpg',  # Make sure this file exists!
    blank=True,
    null=True
)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

