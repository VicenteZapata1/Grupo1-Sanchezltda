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
