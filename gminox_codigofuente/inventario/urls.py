from django.urls import path
from django.conf.urls import url,re_path
from . import views

urlpatterns = [
    path(r'materiales/', views.HomeMaterialesView.as_view(), name='materiales'),
    url(r'^material/create/$', views.MaterialCreate.as_view(success_url='/materiales/'),name='material_create'),
    url(r'material/(?P<pk>\d+)/update/$',views.MaterialUpdate.as_view(success_url='/materiales/'), name='material_update'),
    url(r'material/(?P<pk>\d+)/delete/$',views.MaterialDelete.as_view(success_url='/materiales/'), name='material_delete'),
    re_path(r'^material/(?P<id>[0-9]{1})/$', views.DetalleMaterialView.as_view(),name="detalle"),
]
