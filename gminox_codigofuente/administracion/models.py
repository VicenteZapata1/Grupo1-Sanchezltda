from django.db import models

class Cliente(models.Model):
    nombre=models.CharField(max_length=60)
    telefono_cliente=models.CharField(max_length=12)
    rut=models.CharField(max_length=11)
    email_cliente=models.CharField(max_length=60)
    representante=models.CharField(max_length=60)
    telefono_representante=models.CharField(max_length=12)
    email_representante=models.CharField(max_length=60)
    direccion=models.CharField(max_length=60)
    giro=models.CharField(max_length=60)
    clientes=models.Manager()

    def buscar_cliente(nombre,representante):
        busquedas=[]
        datos=Cliente.clientes.raw("SELECT * FROM administracion_cliente WHERE nombre LIKE '%{0}%' and representante LIKE '%{1}%'".format(nombre, representante))
        for dato in datos:
            busquedas.append(dato)
        return busquedas
    
    def __str__(self):
        return "{}".format(self.nombre)