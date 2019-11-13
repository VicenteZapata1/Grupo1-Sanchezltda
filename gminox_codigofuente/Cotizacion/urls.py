from django.urls import path
from django.conf.urls import url,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('upload/', views.upload, name='upload'),
    path('cotizaciones/', views.cotizacion_list, name='cotizacion_list'),
    path('cotizaciones/upload', views.upload_cotizacion, name='uploadcotizacion'),
]

if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)