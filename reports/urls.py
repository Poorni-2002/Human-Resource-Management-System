from django.urls import path
from . import views

app_name = 'reports'

urlpatterns = [
    path('list/', views.report_list, name='report_list'),
    path('create/', views.report_create, name='report_create'),
    path('update/<int:pk>/', views.report_update, name='report_update'),
    path('download/<int:pk>/', views.report_download, name='report_download'),
    path('generate/<int:pk>/', views.report_generate, name='report_generate'),

]
