from django.shortcuts import render
from django.views.generic import TemplateView
#from .models import Material, EPP, Herramienta, Insumo
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request,'index.html', context= None)

