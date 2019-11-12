from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre=models.CharField(max_length=60)
    rut=models.CharField(max_length=11)
    telefono=models.CharField(max_length=20)
    direccion=models.CharField(max_length=60)
    email=models.CharField(max_length=60)
    giro=models.CharField(max_length=60)
    ciudad=models.CharField(max_length=30)
    contacto=models.CharField(max_length=60)

    def __str__(self):
        return "{}".format(self.nombre)

