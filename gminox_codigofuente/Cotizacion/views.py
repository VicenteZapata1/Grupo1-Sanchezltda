from django.shortcuts import render, redirect
from django.views.generic import TemplateView,ListView,CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from .forms import CotizacionForm
from .models import CotizacionGminox


# Create your views here.



class Upload_PDF(TemplateView):
    template_name ='upload_PDF'


def upload(request):
     context = {}
     if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
     return render(request, 'Cotizacion/upload.html', context)

def cotizacion_list(request):
    cotizaciones =CotizacionGminox.objects.all( )
    return render(request, 'Cotizacion/cotizacion_list.html', {
        'cotizaciones': cotizaciones
    })

def upload_cotizacion(request):
    if request.method == 'POST': 
        form = CotizacionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cotizacion_list')
    else:
        form = CotizacionForm()
    return render(request, 'Cotizacion/uploadcotizacion.html',{
        'form': form
    })