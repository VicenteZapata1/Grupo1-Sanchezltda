from django.db import models
from django.core.validators import FileExtensionValidator
import datetime

# Create your models here.
class FacturaCompraGminox(models.Model):
    Proveedor = models.CharField(max_length=100)
    NumeroFactura = models.PositiveIntegerField( null= True, blank= True, default=0)
    Fecha= models.DateField(("Date"), default=datetime.date.today)
    Monto = models.BigIntegerField( null= True, blank= True, default=0)
    Iva = models.BigIntegerField( null= True, blank= True, default=0)
    Total = models.BigIntegerField( null= True, blank= True, default=0)

    pdf = models.FileField(upload_to='facturascompra/', validators=[FileExtensionValidator(['pdf'])])

    def __str__(self): 

        return self.Proveedor

class FacturaVentaGminox(models.Model):
    Cliente = models.CharField(max_length=100)
    NumeroFactura = models.PositiveIntegerField( null= True, blank= True, default=0)
    Fecha= models.DateField(("Date"), default=datetime.date.today)
    Monto = models.BigIntegerField( null= True, blank= True, default=0)
    Iva = models.BigIntegerField( null= True, blank= True, default=0)
    Total = models.BigIntegerField( null= True, blank= True, default=0)

    pdf = models.FileField(upload_to='facturasventa/', validators=[FileExtensionValidator(['pdf'])])


    def __str__(self): 

        return self.Cliente