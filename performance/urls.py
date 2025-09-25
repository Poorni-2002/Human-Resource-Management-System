from django.urls import path
from . import views

app_name = 'performance'

urlpatterns = [
    path('', views.performance_list, name='performance_list'),
    path('create/', views.performance_create, name='performance_create'),
    path('update/<int:pk>/', views.performance_update, name='performance_update'),
    path('delete/<int:pk>/', views.performance_delete, name='performance_delete'),
]
