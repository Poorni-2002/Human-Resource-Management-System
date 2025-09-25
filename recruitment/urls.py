from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "recruitment" 

urlpatterns = [
    # Public
    path('vacancies/', views.public_vacancy_list, name='vacancy_list'),
    path('vacancy/<int:pk>/', views.vacancy_detail, name='vacancy_detail'),
    path('vacancy/<int:pk>/apply/', views.apply_vacancy, name='apply_vacancy'),

    # Admin
    path('admin/vacancies/', views.vacancy_list_admin, name='vacancy_list_admin'),
    path('admin/vacancy/create/', views.vacancy_create, name='vacancy_create'),
    path('admin/vacancy/<int:pk>/edit/', views.vacancy_update, name='vacancy_update'),
    path('admin/vacancy/<int:pk>/delete/', views.vacancy_confirm_delete, name='vacancy_delete'),
    path('admin/applications/', views.application_list_admin, name='application_list_admin'),
    path('offer-letter/<int:application_id>/', views.generate_offer_letter_pdf, name='generate_offer_letter'),
    path('applications/', views.application_list_admin, name='application_list'),
    path('applications/<int:pk>/status/<str:new_status>/', views.update_application_status, name='update_application_status'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)