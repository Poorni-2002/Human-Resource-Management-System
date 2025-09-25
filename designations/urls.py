from django.urls import path
from . import views

app_name = 'designations'

urlpatterns = [
    path('', views.designation_list, name='designation_list'),
    path('create/', views.designation_create, name='designation_create'),
    path('update/<int:pk>/', views.designation_update, name='designation_update'),
    path('delete/<int:pk>/', views.designation_delete, name='designation_delete'),
]
