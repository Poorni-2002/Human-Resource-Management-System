from django.urls import path
from . import views

app_name = 'attendances'

urlpatterns = [
    path('', views.attendance_list, name='attendances_list'),
    path('add/', views.attendance_create, name='attendance_add'),
    path('<int:pk>/edit/', views.attendance_update, name='attendance_update'),
    path('<int:pk>/delete/', views.attendance_delete, name='attendance_delete'),
]
