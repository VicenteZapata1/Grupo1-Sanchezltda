from django.urls import path
from django.conf.urls import url,re_path
from . import views

urlpatterns = [
    path(r'materiales/', views.HomeMaterialesView.as_view(), name='materiales'),
    url(r'^material/create/$', views.MaterialCreate.as_view(success_url='/materiales/'),name='material_create'),
    url(r'material/(?P<pk>\d+)/update/$',views.MaterialUpdate.as_view(success_url='/materiales/'), name='material_update'),
    url(r'material/(?P<pk>\d+)/delete/$',views.MaterialDelete.as_view(success_url='/materiales/'), name='material_delete'),
    re_path(r'^material/(?P<id>[0-9]{1})/$', views.DetalleMaterialView.as_view(),name="detalle"),
    url(r'epps/', views.HomeEPPView.as_view(),name='epps'),
    url(r'^epp/create/$', views.EPPCreate.as_view(success_url='/epps/'),name='epp_create'),
    url(r'^epp/(?P<pk>\d+)/update/$', views.EPPUpdate.as_view(success_url='/epps/'),name='epp_update'),
    url(r'^epp/(?P<pk>\d+)/delete/$', views.EPPDelete.as_view(success_url='/epps/'),name='epp_delete'),
    re_path(r'^epp/(?P<id>[0-9]{1})/$', views.DetalleEPPView.as_view(),name="detalle"),
    url(r'herramientas/', views.HomeHerramientasView.as_view(),name='herramientas'),
    url(r'^herramienta/create/$', views.HerramientaCreate.as_view(success_url='/herramientas/'),name='herramienta_create'),
    url(r'^herramienta/(?P<pk>\d+)/update/$', views.HerramientaUpdate.as_view(success_url='/herramientas/'),name='herramienta_update'),
    url(r'^herramienta/(?P<pk>\d+)/delete/$', views.HerramientaDelete.as_view(success_url='/herramientas/'),name='herramienta_delete'),
    re_path(r'^herramienta/(?P<id>[0-9]{1})/$', views.DetalleHerramientaView.as_view(),name="detalle"),
    url(r'insumos/', views.HomeInsumosView.as_view(),name='insumos'),
    url(r'^insumo/create/$', views.InsumoCreate.as_view(success_url='/insumos/'),name='insumo_create'),
    url(r'^insumo/(?P<pk>\d+)/update/$', views.InsumoUpdate.as_view(success_url='/insumos/'),name='insumo_update'),
    url(r'^insumo/(?P<pk>\d+)/delete/$', views.InsumoDelete.as_view(success_url='/insumos/'),name='insumo_delete'),
    re_path(r'^insumo/(?P<id>[0-9]{1})/$', views.DetalleInsumoView.as_view(),name="detalle"),
    url(r'despuntes/', views.HomeDespuntesView.as_view(),name='despuntes'),
    url(r'^despunte/create/$', views.DespunteCreate.as_view(success_url='/despuntes/'),name='despunte_create'),
    url(r'^despunte/(?P<pk>\d+)/update/$', views.DespunteUpdate.as_view(success_url='/despuntes/'),name='despunte_update'),
    url(r'^despunte/(?P<pk>\d+)/delete/$', views.DespunteDelete.as_view(success_url='/despuntes/'),name='despunte_delete'),
    re_path(r'^despunte/(?P<id>[0-9]{1})/$', views.DetalleDespunteView.as_view(),name="detalle"),

]
