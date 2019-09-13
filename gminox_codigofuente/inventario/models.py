from django.db import models
import datetime
# Create your models here.

class Material(models.Model):
    nombre=models.CharField(max_length=60)
    cantidad=models.IntegerField()
    largo=models.IntegerField()
    ancho=models.IntegerField()
    espesor=models.IntegerField()
    materiales=models.Manager()

    def __str__(self):
        return "{}".format(self.nombre)

class EPP(models.Model):
    nombre=models.CharField(max_length=60)
    cantidad=models.IntegerField()
    marca=models.CharField(max_length=20, default="Generico")
    umedida=models.CharField(max_length=20, null= True, blank= True, default="Talla")
    medida=models.IntegerField(null= True, blank= True)
    fecha= models.DateField(("Date"), default=datetime.date.today)
    epps=models.Manager()

    def __str__(self):
        return "{}".format(self.nombre)

class Herramienta(models.Model):
    nombre=models.CharField(max_length=60)
    cantidad=models.IntegerField()
    marca=models.CharField(max_length=20, default="Generico")
    umedida=models.CharField(max_length=20, null= True, blank= True,)
    medida=models.IntegerField(null= True, blank= True)
    fecha= models.DateField(("Date"), default=datetime.date.today)
    def __str__(self):
        return "{}".format(self.nombre)      

class Insumo(models.Model):
    nombre=models.CharField(max_length=60)
    cantidad=models.IntegerField()
    marca=models.CharField(max_length=20, default="Generico")
    umedida=models.CharField(max_length=20, null= True, blank= True)
    medida=models.IntegerField(null= True, blank= True)
    fecha= models.DateField(("Date"), default=datetime.date.today)
    def __str__(self):
        return "{}".format(self.nombre)          

class Despunte(models.Model):
    nombre=models.CharField(max_length=60)
    cantidad=models.IntegerField()
    largo=models.IntegerField()
    ancho=models.IntegerField()
    espesor=models.IntegerField()
    despuntes=models.Manager()

    def __str__(self):
        return "{}".format(self.nombre)
