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


class Proveedor(models.Model):
    nombre=models.CharField(max_length=60)
    telefono_proveedor=models.CharField(max_length=12)
    rut=models.CharField(max_length=11)
    email_proveedor=models.CharField(max_length=60)
    representante=models.CharField(max_length=60)
    vendedor=models.CharField(max_length=60)
    telefono_representante=models.CharField(max_length=12)
    email_representante=models.CharField(max_length=60)
    telefono_vendedor=models.CharField(max_length=12)
    email_vendedor=models.CharField(max_length=60)
    direccion=models.CharField(max_length=60)
    giro=models.CharField(max_length=60)
    proveedores=models.Manager()

    def buscar_proveedor(nombre,vendedor):
        busquedas=[]
        datos=Proveedor.proveedores.raw("SELECT * FROM administracion_proveedor WHERE nombre LIKE '%{0}%' and vendedor LIKE '%{1}%'".format(nombre, vendedor))
        for dato in datos:
            busquedas.append(dato)
        return busquedas
    
    def __str__(self):
        return "{}".format(self.nombre)        