from django.shortcuts import render, redirect
from django.views.generic import TemplateView,ListView,CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from .forms import FacturaCompraForm
from .forms import FacturaVentaForm
from .models import FacturaCompraGminox
from .models import FacturaVentaGminox
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


# Create your views here.

def test_func(request):
    return request.groups.filter(name="Oficina").exists()

        
class Upload_PDF(TemplateView):
    template_name ='upload_PDF'

@user_passes_test(test_func)
def upload(request):
     context = {}
     if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)#ruta del pdf
        context['url'] = fs.url(name)
     return render(request, 'facturas/upload.html', context)

@user_passes_test(test_func)
def facturacompra_list(request):
    facturascompra = FacturaCompraGminox.objects.all( )
    return render(request, 'facturas/facturacompra_list.html', {
        'facturascompra': facturascompra
    })

@user_passes_test(test_func)
def upload_facturacompra(request):
    if request.method == 'POST': 
        form = FacturaCompraForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('facturacompra_list')
    else:
        form = FacturaCompraForm()
    return render(request, 'facturas/uploadfacturacompra.html',{
        'form': form
    })

@user_passes_test(test_func)
def uploadVenta(request):
     context = {}
     if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)#ruta del pdf
        context['url'] = fs.url(name)
     return render(request, 'facturas/uploadventa.html', context)

@user_passes_test(test_func)
def facturaventa_list(request):
    facturasventa = FacturaVentaGminox.objects.all( )
    return render(request, 'facturas/facturaventa_list.html', {
        'facturasventa': facturasventa
    })

@user_passes_test(test_func)
def upload_facturaventa(request):
    if request.method == 'POST': 
        form2 = FacturaVentaForm(request.POST, request.FILES)
        if form2.is_valid():
            form2.save()
            return redirect('facturaventa_list')
    else:
        form2 = FacturaVentaForm()
    return render(request, 'facturas/uploadfacturaventa.html',{
        'form2': form2
    })