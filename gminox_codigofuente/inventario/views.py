from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Material #, EPP, Herramienta, Insumo
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