from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Material,EPP,Herramienta,Insumo,Despunte
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.conf import settings
from django.conf.urls.static import static

# Create your views here.

urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


class HomeMaterialesView(LoginRequiredMixin,TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'inventario/materiales.html', {'materiales': Material.materiales.all()})

class DetalleMaterialView(LoginRequiredMixin,TemplateView):
    def get(self, request, **kwargs):
        id=kwargs["id"]
        return render(request, 'inventario/material.html', {'material': Material.materiales.get(id=id)})

class MaterialCreate(CreateView):
    model = Material
    template_name='./inventario/material_form.html'
    fields = '__all__'

class MaterialUpdate(UpdateView):
    model = Material
    template_name='./inventario/material_form.html'
    fields = ['nombre','cantidad','largo','ancho','espesor']

class MaterialDelete(DeleteView):
    model = Material
    template_name='./inventario/material_form.html'
    success_url = reverse_lazy('materiales')        

 
class HomeEPPView(LoginRequiredMixin,TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'inventario/epps.html',{'epps': EPP.epps.all()})

class DetalleEPPView(LoginRequiredMixin,TemplateView):
    def get(self, request, **kwargs):
        id=kwargs["id"]
        return render(request, 'inventario/epp.html', {'epp': EPP.epps.get(id=id)})   

class EPPCreate(CreateView):
    model = EPP
    template_name='./inventario/epp_form.html'
    fields = '__all__'

class EPPUpdate(UpdateView):
    model = EPP
    template_name='./inventario/epp_form.html'
    fields = ['nombre','cantidad']

class EPPDelete(DeleteView):
    model = EPP
    template_name='./inventario/epp_form.html'
    success_url = reverse_lazy('epps')

class HomeHerramientasView(LoginRequiredMixin,TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'inventario/herramientas.html',{'herramientas': Herramienta.herramientas.all()})

class DetalleHerramientaView(LoginRequiredMixin,TemplateView):
    def get(self, request, **kwargs):
        id=kwargs["id"]
        return render(request, 'inventario/herramienta.html', {'herramienta': Herramienta.herramientas.get(id=id)})

class HerramientaCreate(CreateView):
    model = Herramienta
    template_name='./inventario/herramienta_form.html'
    fields = '__all__'

class HerramientaUpdate(UpdateView):
    model = Herramienta
    template_name='./inventario/herramienta_form.html'
    fields = ['nombre','cantidad']

class HerramientaDelete(DeleteView):
    model = Herramienta
    template_name='./inventario/herramienta_form.html'
    success_url = reverse_lazy('herramientas')

class HomeInsumosView(LoginRequiredMixin,TemplateView):
    def get(self,request, **kwargs):
        return render(request, 'inventario/insumos.html',{'insumos':Insumo.insumos.all()})

class DetalleInsumoView(LoginRequiredMixin,TemplateView):
    def get(self, request, **kwargs):
        id=kwargs["id"]
        return render(request, 'inventario/insumo.html', {'insumo': Insumo.insumos.get(id=id)})

class InsumoCreate(CreateView):
    model = Insumo
    template_name='./inventario/insumo_form.html'
    fields = '__all__'

class InsumoUpdate(UpdateView):
    model = Insumo
    template_name='./inventario/insumo_form.html'
    fields = ['nombre','medida','cantidad']    

class InsumoDelete(DeleteView):
    model = Insumo
    template_name='./inventario/insumo_form.html'
    success_url = reverse_lazy('insumos')

class HomeDespuntesView(LoginRequiredMixin,TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'inventario/despuntes.html', {'despuntes': Despunte.despuntes.all()})

class DetalleDespunteView(LoginRequiredMixin,TemplateView):
    def get(self, request, **kwargs):
        id=kwargs["id"]
        return render(request, 'inventario/despunte.html', {'despunte': Despunte.despuntes.get(id=id)})

class DespunteCreate(CreateView):
    model = Despunte
    template_name='./inventario/despunte_form.html'
    fields = '__all__'

class DespunteUpdate(UpdateView):
    model = Despunte
    template_name='./inventario/despunte_form.html'
    fields = ['nombre','cantidad','largo','ancho','espesor']

class DespunteDelete(DeleteView):
    model = Despunte
    template_name='./inventario/despunte_form.html'
    success_url = reverse_lazy('despuntes')        

class BuscarDespunte(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'inventario/despunte_buscar.html', {'despuntes': Despunte.despuntes.all()})