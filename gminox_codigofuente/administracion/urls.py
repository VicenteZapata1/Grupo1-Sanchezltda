from django.urls import path
from django.conf.urls import url,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(r'clientes/', views.HomeClientesView.as_view(), name='clientes'),
    url(r'^cliente/create/$', views.ClienteCreate.as_view(success_url='/clientes/'),name='cliente_create'),
    url(r'cliente/(?P<pk>\d+)/update/$',views.ClienteUpdate.as_view(success_url='/clientes/'), name='cliente_update'),
    url(r'cliente/(?P<pk>\d+)/delete/$',views.ClienteDelete.as_view(success_url='/clientes/'), name='cliente_delete'),
    re_path(r'^cliente/(?P<id>[0-9]{1})/$', views.DetalleClienteView.as_view(),name="detalle"),
    re_path(r'^cliente/buscar/$', views.BuscarCliente.as_view(),name ='buscar_cliente'),
    re_path(r'^cliente/buscar/detalles/', views.BuscarClienteDetalle.as_view(),name ='buscar_cliente_detalle'),
        
]



if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)