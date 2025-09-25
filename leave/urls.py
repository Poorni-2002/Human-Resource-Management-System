from django.urls import path
from . import views

app_name = 'leave'

urlpatterns = [
    path('', views.leave_list, name='leave_list'),
    path('create/', views.leave_create, name='leave_create'),
    path('update/<int:pk>/', views.leave_update, name='leave_update'),
    path('delete/<int:pk>/', views.leave_delete, name='leave_delete'),
    path('my_leaves/', views.my_leaves, name='my_leaves'),
    path('approve/<int:pk>/', views.leave_approve, name='leave_approve'),
    path('reject/<int:pk>/', views.leave_reject, name='leave_reject'),
]
