from django.shortcuts import render, redirect
from django.views.generic import TemplateView,ListView,CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from .forms import CotizacionForm
from .models import CotizacionGminox
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
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
     return render(request, 'Cotizacion/upload.html', context)
@user_passes_test(test_func)
def cotizacion_list(request):
    cotizaciones =CotizacionGminox.objects.all( )
    return render(request, 'Cotizacion/cotizacion_list.html', {
        'cotizaciones': cotizaciones
    })
@user_passes_test(test_func)
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