from django.shortcuts import render
from django.views.generic import TemplateView
from administracion.models import Cliente
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from django.core.files.storage import FileSystemStorage

class HomeClientesView(LoginRequiredMixin,TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'administracion/clientes.html', {'clientes': Cliente.clientes.all()})

class DetalleClienteView(LoginRequiredMixin,TemplateView):
    def get(self, request, **kwargs):
        id=kwargs["id"]
        return render(request, 'administracion/cliente.html', {'cliente': Cliente.clientes.get(id=id)})
class ClienteCreate(CreateView):
    model = Cliente
    template_name='./administracion/cliente_form.html'
    fields = '__all__'

class ClienteUpdate(UpdateView):
    model = Cliente
    template_name='./administracion/cliente_form.html'
    fields = ['representante', 'telefono_representante','email_representante','direccion']

class ClienteDelete(DeleteView):
    model = Cliente
    template_name='./administracion/cliente_form.html'
    success_url = reverse_lazy('clientes')  

class BuscarCliente(TemplateView):
    model = Cliente
    template_name='./administracion/cliente_buscar.html'
    fields = ['nombre','representante']


class BuscarClienteDetalle(TemplateView):
    def post(self, request, **kwargs):
        nombre=request.POST.get("nombre")
        representante=request.POST.get("representante")    
        listas=Cliente.buscar_cliente(nombre,representante)
        for lista in listas:
            print(lista)
        return render(request, 'administracion/cliente_detalle.html', {'clientes':listas})

