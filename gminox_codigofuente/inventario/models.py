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

    def buscar_epp(nombre):
        epps=[]
        datos=EPP.epps.raw("SELECT * FROM inventario_epp WHERE nombre LIKE '%{0}%'".format(nombre))
        return datos

    def __str__(self):
        return "{}".format(self.nombre)

class Herramienta(models.Model):
    nombre=models.CharField(max_length=60)
    cantidad=models.IntegerField()
    marca=models.CharField(max_length=20, default="Generico")
    umedida=models.CharField(max_length=20, null= True, blank= True,)
    medida=models.IntegerField(null= True, blank= True)
    fecha= models.DateField(("Date"), default=datetime.date.today)
    herramientas=models.Manager()

    def __str__(self):
        return "{}".format(self.nombre)      

class Insumo(models.Model):
    nombre=models.CharField(max_length=60)
    cantidad=models.IntegerField()
    marca=models.CharField(max_length=20, default="Generico")
    umedida=models.CharField(max_length=20, null= True, blank= True)
    medida=models.IntegerField(null= True, blank= True)
    fecha= models.DateField(("Date"), default=datetime.date.today)
    insumos= models.Manager()

    def __str__(self):
        return "{}".format(self.nombre)          

class Despunte(models.Model):
    nombre=models.CharField(max_length=60)
    largo=models.IntegerField()
    ancho=models.IntegerField()
    espesor=models.IntegerField()
    despuntes=models.Manager()

    def buscar_despuntes(nombre,largo,ancho,espesor):
        despuntes=[]
        datos=Despunte.despuntes.raw("SELECT * FROM inventario_despunte WHERE nombre LIKE '%{0}%' and largo >= '{1}' and ancho >= '{2}' and espesor = '{3}'".format(nombre, largo, ancho, espesor))
        for despunte in datos:
            despuntes.append(despunte)
        return despuntes
    
    def __str__(self):
        return "{}".format(self.nombre)
   
    def __str__(self):
        return "{}".format(self.nombre)