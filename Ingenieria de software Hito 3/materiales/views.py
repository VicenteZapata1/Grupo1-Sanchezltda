from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Material, EPP, Herramienta, Insumo
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request,'index.html', context= None)

class HomeMaterialesView(LoginRequiredMixin,TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'materiales.html', {'materiales': Material.materiales.all()})

class DetalleMaterialView(LoginRequiredMixin,TemplateView):
    def get(self, request, **kwargs):
        identificador=kwargs["identificador"]
        return render(request, 'material.html', {'material': Material.materiales.get(identificador=identificador)})

class HomeEPPView(LoginRequiredMixin,TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'epps.html',{'epps': EPP.epps.all()})

class DetalleEPPView(LoginRequiredMixin,TemplateView):
    def get(self, request, **kwargs):
        identificador=kwargs["identificador"]
        return render(request, 'epp.html', {'epp': EPP.epps.get(identificador=identificador)})

class HomeHerramientasView(LoginRequiredMixin,TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'herramientas.html',{'herramientas': Herramienta.herramientas.all()})

class DetalleHerramientaView(LoginRequiredMixin,TemplateView):
    def get(self, request, **kwargs):
        identificador=kwargs["identificador"]
        return render(request, 'herramienta.html', {'herramienta': Herramienta.herramientas.get(identificador=identificador)})

class HomeInsumosView(LoginRequiredMixin,TemplateView):
    def get(self,request, **kwargs):
        return render(request, 'insumos.html',{'insumos':Insumo.insumos.all()})

class DetalleInsumoView(LoginRequiredMixin,TemplateView):
    def get(self, request, **kwargs):
        identificador=kwargs["identificador"]
        return render(request, 'insumo.html', {'insumo': Insumo.insumos.get(identificador=identificador)})

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