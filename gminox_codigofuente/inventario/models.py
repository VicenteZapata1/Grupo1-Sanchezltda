from django.db import models
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
    epps=models.Manager()
    def __str__(self):
        return "{}".format(self.nombre)

class Herramienta(models.Model):
    nombre=models.CharField(max_length=60)
    cantidad=models.IntegerField()
    herramientas=models.Manager()
    def __str__(self):
        return "{}".format(self.nombre)      

class Insumo(models.Model):
    nombre=models.CharField(max_length=60)
    medida=models.FloatField()
    cantidad=models.IntegerField()
    insumos=models.Manager()
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
