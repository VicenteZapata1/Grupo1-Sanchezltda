from django.shortcuts import render
from django.views.generic import TemplateView
from administracion.models import Cliente, Proveedor
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

class HomeProveedoresView(LoginRequiredMixin,TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'administracion/proveedores.html', {'proveedores': Proveedor.proveedores.all()})

class DetalleProveedorView(LoginRequiredMixin,TemplateView):
    def get(self, request, **kwargs):
        id=kwargs["id"]
        return render(request, 'administracion/proveedor.html', {'proveedor': Proveedor.proveedores.get(id=id)})

class ProveedorCreate(CreateView):
    model = Proveedor
    template_name='./administracion/proveedor_form.html'
    fields = '__all__'

class ProveedorUpdate(UpdateView):
    model = Proveedor
    template_name='./administracion/proveedor_form.html'
    fields = ['vendedor', 'telefono_vendedor','email_vendedor','direccion']

class ProveedorDelete(DeleteView):
    model = Proveedor
    template_name='./administracion/proveedor_form.html'
    success_url = reverse_lazy('proveedores')  

class BuscarProveedor(TemplateView):
    model = Proveedor
    template_name='./administracion/proveedor_buscar.html'
    fields = ['nombre','vendedor']        

class BuscarProveedorDetalle(TemplateView):
    def post(self, request, **kwargs):
        nombre=request.POST.get("nombre")
        vendedor=request.POST.get("vendedor")    
        listas=Proveedor.buscar_proveedor(nombre,vendedor)
        for lista in listas:
            print(lista)
        return render(request, 'administracion/proveedor_detalle.html', {'proveedores':listas})    

