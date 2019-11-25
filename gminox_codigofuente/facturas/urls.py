from django.urls import path
from django.conf.urls import url,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('upload/', views.upload, name='upload'),
    path('facturas/', views.facturacompra_list, name='facturacompra_list'),
    path('facturas/upload', views.upload_facturacompra, name='uploadfacturacompra'),
    path('uploadventa/', views.uploadVenta, name='uploadventa'),
    path('facturaventa/', views.facturaventa_list, name='facturaventa_list'),
    path('facturas/uploadventa', views.upload_facturaventa, name='uploadfacturaventa'),
]

if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)