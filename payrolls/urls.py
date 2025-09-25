from django.urls import path
from . import views

app_name = 'payrolls'

urlpatterns = [
    path('', views.payroll_list, name='payroll_list'),
    path('generate/', views.create_monthly_payrolls, name='create_monthly_payrolls'),
    path('export/pdf/', views.export_payroll_pdf, name='export_payroll_pdf'), 
    path('my_payrolls/', views.my_payroll, name='my_payrolls'),
]