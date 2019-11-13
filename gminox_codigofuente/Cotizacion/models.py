from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class CotizacionGminox(models.Model):
    Cliente = models.CharField(max_length=100)
    NumeroCotizacion = models.PositiveIntegerField()
    pdf = models.FileField(upload_to='cotizaciones/', validators=[FileExtensionValidator(['pdf'])])

    def __str__(self): 

        return self.Cliente
    