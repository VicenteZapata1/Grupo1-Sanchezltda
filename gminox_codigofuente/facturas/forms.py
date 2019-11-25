from django import forms
from .models import FacturaCompraGminox
from .models import FacturaVentaGminox

class FacturaVentaForm(forms.ModelForm):
    class Meta:
        model = FacturaVentaGminox
        fields = ('Cliente','NumeroFactura','Monto','Iva','Total','pdf')


class FacturaCompraForm(forms.ModelForm):
    class Meta:
        model = FacturaCompraGminox
        fields = ('Proveedor','NumeroFactura','Monto','Iva','Total','pdf')

