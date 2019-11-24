from django.shortcuts import render
from django.views.generic import TemplateView
from administracion.models import Cliente, Proveedor
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


class EsMiembro(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name="Oficina").exists()


class HomeClientesView(LoginRequiredMixin,EsMiembro,TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'administracion/clientes.html', {'clientes': Cliente.clientes.all()})

class DetalleClienteView(LoginRequiredMixin,EsMiembro,TemplateView):
    def get(self, request, **kwargs):
        id=kwargs["id"]
        return render(request, 'administracion/cliente.html', {'cliente': Cliente.clientes.get(id=id)})
class ClienteCreate(EsMiembro,CreateView):
    model = Cliente
    template_name='./administracion/cliente_form.html'
    fields = '__all__'

class ClienteUpdate(EsMiembro,UpdateView):
    model = Cliente
    template_name='./administracion/cliente_form.html'
    fields = ['representante', 'telefono_representante','email_representante','direccion']

class ClienteDelete(EsMiembro,DeleteView):
    model = Cliente
    template_name='./administracion/cliente_form.html'
    success_url = reverse_lazy('clientes')  

class BuscarCliente(EsMiembro,TemplateView):
    model = Cliente
    template_name='./administracion/cliente_buscar.html'
    fields = ['nombre','representante']


class BuscarClienteDetalle(EsMiembro,TemplateView):
    def post(self, request, **kwargs):
        nombre=request.POST.get("nombre")
        representante=request.POST.get("representante")    
        listas=Cliente.buscar_cliente(nombre,representante)
        for lista in listas:
            print(lista)
        return render(request, 'administracion/cliente_detalle.html', {'clientes':listas})

class HomeProveedoresView(LoginRequiredMixin,EsMiembro,TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'administracion/proveedores.html', {'proveedores': Proveedor.proveedores.all()})

class DetalleProveedorView(LoginRequiredMixin,EsMiembro,TemplateView):
    def get(self, request, **kwargs):
        id=kwargs["id"]
        return render(request, 'administracion/proveedor.html', {'proveedor': Proveedor.proveedores.get(id=id)})

class ProveedorCreate(EsMiembro,CreateView):
    model = Proveedor
    template_name='./administracion/proveedor_form.html'
    fields = '__all__'

class ProveedorUpdate(EsMiembro,UpdateView):
    model = Proveedor
    template_name='./administracion/proveedor_form.html'
    fields = ['vendedor', 'telefono_vendedor','email_vendedor','direccion']

class ProveedorDelete(EsMiembro,DeleteView):
    model = Proveedor
    template_name='./administracion/proveedor_form.html'
    success_url = reverse_lazy('proveedores')  

class BuscarProveedor(EsMiembro,TemplateView):
    model = Proveedor
    template_name='./administracion/proveedor_buscar.html'
    fields = ['nombre','vendedor']        

class BuscarProveedorDetalle(EsMiembro,TemplateView):
    def post(self, request, **kwargs):
        nombre=request.POST.get("nombre")
        vendedor=request.POST.get("vendedor")    
        listas=Proveedor.buscar_proveedor(nombre,vendedor)
        for lista in listas:
            print(lista)
        return render(request, 'administracion/proveedor_detalle.html', {'proveedores':listas})    

