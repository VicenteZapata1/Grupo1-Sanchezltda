from django.shortcuts import render, redirect
from django.views.generic import TemplateView,ListView,CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from .forms import FacturaCompraForm
from .forms import FacturaVentaForm
from .models import FacturaCompraGminox
from .models import FacturaVentaGminox


# Create your views here.
class Upload_PDF(TemplateView):
    template_name ='upload_PDF'


def upload(request):
     context = {}
     if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)#ruta del pdf
        context['url'] = fs.url(name)
     return render(request, 'facturas/upload.html', context)

def facturacompra_list(request):
    facturascompra = FacturaCompraGminox.objects.all( )
    return render(request, 'facturas/facturacompra_list.html', {
        'facturascompra': facturascompra
    })

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

def uploadVenta(request):
     context = {}
     if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)#ruta del pdf
        context['url'] = fs.url(name)
     return render(request, 'facturas/uploadventa.html', context)

def facturaventa_list(request):
    facturasventa = FacturaVentaGminox.objects.all( )
    return render(request, 'facturas/facturaventa_list.html', {
        'facturasventa': facturasventa
    })

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