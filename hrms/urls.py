from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('designations/', include('designations.urls')),
    path('employees/', include('employees.urls')),
    path('performance/', include('performance.urls')),
    path('leave/', include('leave.urls')),
    path('reports/', include('reports.urls',namespace='reports',)),
    path('recruitment/', include('recruitment.urls',namespace='recruitment')),
    path('attendances/', include('attendances.urls')),
    path('payrolls/', include('payrolls.urls',namespace='payrolls')),

    path('', lambda request: redirect('accounts/login/', permanent=False)),
    path('login/', lambda request: redirect('accounts/login/', permanent=False)),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)