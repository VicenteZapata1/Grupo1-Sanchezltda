from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Material,EPP,Herramienta,Insumo,Despunte
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

# Create your views here.

urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

class EsMiembro(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name="Oficina").exists()


class HomeMaterialesView(LoginRequiredMixin,TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'inventario/materiales.html', {'materiales': Material.materiales.all()})

class DetalleMaterialView(LoginRequiredMixin,TemplateView):
    def get(self, request, **kwargs):
        id=kwargs["id"]
        return render(request, 'inventario/material.html', {'material': Material.materiales.get(id=id)})

class MaterialCreate(EsMiembro,CreateView):
    model = Material
    template_name='./inventario/material_form.html'
    fields = '__all__'

class MaterialUpdate(EsMiembro,UpdateView):
    model = Material
    template_name='./inventario/material_form.html'
    fields = ['nombre','cantidad','largo','ancho','espesor']

class MaterialDelete(EsMiembro,DeleteView):
    model = Material
    template_name='./inventario/material_form.html'
    success_url = reverse_lazy('materiales')        

class Tipo:
    def __init__(self,codigo,nombre,default):
        self.codigo=codigo
        self.nombre=nombre
        self.default=default


class HomeEPPView(LoginRequiredMixin,TemplateView):

    def generar_tipos(self):
        tipos=[]
        tipos.append(Tipo("","",1))
        tipos.append(Tipo("zapatos","Zapatos de Seguridad",0))
        tipos.append(Tipo("guante","Guante",0))
        tipos.append(Tipo("tapones","Tapones para Oído",0))
        tipos.append(Tipo("antiparra","Antiparra",0))
        tipos.append(Tipo("mascara","Máscara de Soldar",0))
        return tipos

    def get(self, request, **kwargs):
        return render(request, 'inventario/epps.html',{'epps': EPP.epps.all(),'tipos': self.generar_tipos()})

    def post(self, request, **kwargs):
        tipo=request.POST.get("tipo")
        print(tipo)
        if tipo=="":
            return render(request, 'inventario/epps.html',{'epps': EPP.epps.all(), 'tipos': self.generar_tipos()})
        else:
            datos=EPP.buscar_epp(tipo)
            for dato in datos:
                print(dato)
            tipos=self.generar_tipos()
            for tipo2 in tipos:
                if tipo2.codigo==tipo:
                    tipo2.default=1
                else:
                    tipo2.default=0
            tipos=sorted(tipos,key=lambda x : x.default,reverse=True)
            return render(request, 'inventario/epps.html', {'epps':datos, 'tipos': tipos })

class DetalleEPPView(LoginRequiredMixin,TemplateView):
    def get(self, request, **kwargs):
        id=kwargs["id"]
        return render(request, 'inventario/epp.html', {'epp': EPP.epps.get(id=id)})   

class EPPCreate(EsMiembro,CreateView):
    model = EPP
    template_name='./inventario/epp_form.html'
    fields = '__all__'

class EPPUpdate(EsMiembro,UpdateView):
    model = EPP
    template_name='./inventario/epp_form.html'
    fields = ['nombre','cantidad']

class EPPDelete(EsMiembro,DeleteView):
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

class HerramientaCreate(EsMiembro,CreateView):
    model = Herramienta
    template_name='./inventario/herramienta_form.html'
    fields = '__all__'

class HerramientaUpdate(EsMiembro,UpdateView):
    model = Herramienta
    template_name='./inventario/herramienta_form.html'
    fields = ['nombre','cantidad']

class HerramientaDelete(EsMiembro,DeleteView):
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

class InsumoCreate(EsMiembro,CreateView):
    model = Insumo
    template_name='./inventario/insumo_form.html'
    fields = '__all__'

class InsumoUpdate(EsMiembro,UpdateView):
    model = Insumo
    template_name='./inventario/insumo_form.html'
    fields = ['nombre','medida','cantidad']    

class InsumoDelete(EsMiembro,DeleteView):
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

class DespunteCreate(EsMiembro,CreateView):
    model = Despunte
    template_name='./inventario/despunte_form.html'
    fields = '__all__'

class DespunteUpdate(EsMiembro,UpdateView):
    model = Despunte
    template_name='./inventario/despunte_form.html'
    fields = ['nombre','cantidad','largo','ancho','espesor']

class DespunteDelete(EsMiembro,DeleteView):
    model = Despunte
    template_name='./inventario/despunte_form.html'
    success_url = reverse_lazy('despuntes')


class BuscarDespunte(EsMiembro,TemplateView):
    model = Despunte
    template_name='./inventario/despunte_buscar.html'
    fields = ['nombre','largo','ancho','espesor']


class BuscarDespunteDetalle(EsMiembro,TemplateView):
    def post(self, request, **kwargs):
        nombre=request.POST.get("nombre")
        largo=request.POST.get("largo")
        ancho=request.POST.get("ancho")
        espesor=request.POST.get("espesor")        
        datos=Despunte.buscar_despuntes(nombre,largo,ancho,espesor)
        for dato in datos:
            print(dato)
        return render(request, 'inventario/despunte_detalle.html', {'despuntes':datos})
        

class BuscarEPP(EsMiembro,TemplateView):
    model = EPP
    template_name='./inventario/epps.html'
    fields = ['nombre']
