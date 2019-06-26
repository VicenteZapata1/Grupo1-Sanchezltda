from django.conf.urls import url,re_path
from django.urls import path,include
from materiales import views

urlpatterns = [
    url(r'^$',views.HomePageView.as_view(),name='index'),
    url(r'materiales/', views.HomeMaterialesView.as_view(),name='materiales'),
    url(r'epps/', views.HomeEPPView.as_view(),name='epps'),
    url(r'herramientas/', views.HomeHerramientasView.as_view(),name='herramientas'),
    url(r'insumos/', views.HomeInsumosView.as_view(),name='insumos'),
    url(r'^material/create/$', views.MaterialCreate.as_view(success_url='/materiales/'),name='material_create'),
    url(r'material/(?P<pk>\d+)/update/$',views.MaterialUpdate.as_view(success_url='/materiales/'), name='material_update'),
    url(r'material/(?P<pk>\d+)/delete/$',views.MaterialDelete.as_view(success_url='/materiales/'), name='material_delete'),
    url(r'^herramienta/create/$', views.HerramientaCreate.as_view(success_url='/herramientas/'),name='herramienta_create'),
    url(r'^herramienta/(?P<pk>\d+)/update/$', views.HerramientaUpdate.as_view(success_url='/herramientas/'),name='herramienta_update'),
    url(r'^herramienta/(?P<pk>\d+)/delete/$', views.HerramientaDelete.as_view(success_url='/herramientas/'),name='herramienta_delete'),
    url(r'^insumo/create/$', views.InsumoCreate.as_view(success_url='/insumos/'),name='insumo_create'),
    url(r'^insumo/(?P<pk>\d+)/update/$', views.InsumoUpdate.as_view(success_url='/insumos/'),name='insumo_update'),
    url(r'^insumo/(?P<pk>\d+)/delete/$', views.InsumoDelete.as_view(success_url='/insumos/'),name='insumo_delete'),
    url(r'^epp/create/$', views.EPPCreate.as_view(success_url='/epps/'),name='epp_create'),
    url(r'^epp/(?P<pk>\d+)/update/$', views.EPPUpdate.as_view(success_url='/epps/'),name='epp_update'),
    url(r'^epp/(?P<pk>\d+)/delete/$', views.EPPDelete.as_view(success_url='/epps/'),name='epp_delete'),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    re_path(r'^material/(?P<identificador>[0-9]{1})/$', views.DetalleMaterialView.as_view(),name="detalle"),
    re_path(r'^herramienta/(?P<identificador>[0-9]{1})/$', views.DetalleHerramientaView.as_view(),name="detalle"),
    re_path(r'^insumo/(?P<identificador>[0-9]{1})/$', views.DetalleInsumoView.as_view(),name="detalle"),
    re_path(r'^epp/(?P<identificador>[0-9]{1})/$', views.DetalleEPPView.as_view(),name="detalle")
]
