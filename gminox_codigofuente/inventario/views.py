from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Material,EPP,Herramienta,Insumo,Despunte
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
class HomeMaterialesView(LoginRequiredMixin,TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'materiales.html', {'materiales': Material.materiales.all()})

class DetalleMaterialView(LoginRequiredMixin,TemplateView):
    def get(self, request, **kwargs):
        id=kwargs["id"]
        return render(request, 'material.html', {'material': Material.materiales.get(id=id)})

class MaterialCreate(CreateView):
    model = Material
    template_name='./material_form.html'
    fields = '__all__'

class MaterialUpdate(UpdateView):
    model = Material
    template_name='./material_form.html'
    fields = ['nombre','cantidad','largo','ancho','espesor']

class MaterialDelete(DeleteView):
    model = Material
    template_name='./material_form.html'
    success_url = reverse_lazy('materiales')        

 
class HomeEPPView(LoginRequiredMixin,TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'epps.html',{'epps': EPP.epps.all()})

class DetalleEPPView(LoginRequiredMixin,TemplateView):
    def get(self, request, **kwargs):
        id=kwargs["id"]
        return render(request, 'epp.html', {'epp': EPP.epps.get(id=id)})   

class EPPCreate(CreateView):
    model = EPP
    template_name='./epp_form.html'
    fields = '__all__'

class EPPUpdate(UpdateView):
    model = EPP
    template_name='./epp_form.html'
    fields = ['nombre','cantidad']

class EPPDelete(DeleteView):
    model = EPP
    template_name='./epp_form.html'
    success_url = reverse_lazy('epps')

class HomeHerramientasView(LoginRequiredMixin,TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'herramientas.html',{'herramientas': Herramienta.herramientas.all()})

class DetalleHerramientaView(LoginRequiredMixin,TemplateView):
    def get(self, request, **kwargs):
        id=kwargs["id"]
        return render(request, 'herramienta.html', {'herramienta': Herramienta.herramientas.get(id=id)})

class HerramientaCreate(CreateView):
    model = Herramienta
    template_name='./herramienta_form.html'
    fields = '__all__'

class HerramientaUpdate(UpdateView):
    model = Herramienta
    template_name='./herramienta_form.html'
    fields = ['nombre','cantidad']

class HerramientaDelete(DeleteView):
    model = Herramienta
    template_name='./herramienta_form.html'
    success_url = reverse_lazy('herramientas')

class HomeInsumosView(LoginRequiredMixin,TemplateView):
    def get(self,request, **kwargs):
        return render(request, 'insumos.html',{'insumos':Insumo.insumos.all()})

class DetalleInsumoView(LoginRequiredMixin,TemplateView):
    def get(self, request, **kwargs):
        id=kwargs["id"]
        return render(request, 'insumo.html', {'insumo': Insumo.insumos.get(id=id)})

class InsumoCreate(CreateView):
    model = Insumo
    template_name='./insumo_form.html'
    fields = '__all__'

class InsumoUpdate(UpdateView):
    model = Insumo
    template_name='./insumo_form.html'
    fields = ['nombre','medida','cantidad']    

class InsumoDelete(DeleteView):
    model = Insumo
    template_name='./insumo_form.html'
    success_url = reverse_lazy('insumos')

class HomeDespuntesView(LoginRequiredMixin,TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'despuntes.html', {'despuntes': Despunte.despuntes.all()})

class DetalleDespunteView(LoginRequiredMixin,TemplateView):
    def get(self, request, **kwargs):
        id=kwargs["id"]
        return render(request, 'despunte.html', {'despunte': Despunte.despuntes.get(id=id)})

class DespunteCreate(CreateView):
    model = Despunte
    template_name='./despunte_form.html'
    fields = '__all__'

class DespunteUpdate(UpdateView):
    model = Despunte
    template_name='./despunte_form.html'
    fields = ['nombre','cantidad','largo','ancho','espesor']

class DespunteDelete(DeleteView):
    model = Despunte
    template_name='./despunte_form.html'
    success_url = reverse_lazy('despuntes')        
