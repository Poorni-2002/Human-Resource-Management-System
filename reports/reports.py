from django.urls import path
from . import views

urlpatterns = [
    path('<str:period>/', views.report_view, name='report'),
    path('<str:period>/pdf/', views.report_pdf_view, name='report_pdf'),
]
