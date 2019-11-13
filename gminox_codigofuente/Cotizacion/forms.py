from django import forms
from .models import CotizacionGminox

class CotizacionForm(forms.ModelForm):
    class Meta:
        model = CotizacionGminox
        fields = ('Cliente','NumeroCotizacion','pdf')