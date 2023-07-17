from django.db import models

class Post(models.Model):			
    title = models.CharField(max_length=250)
    content = models.TextField()

    def __str__(self):
        return self.title
    
class Producto(models.Model):
     
    numeroProducto = models.CharField(max_length=24, primary_key=True)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'productos'

class Orden(models.Model):
    numeroOrden = models.IntegerField(max_length=100,primary_key=True)
    #fecha = models.DateField()
    fecha = models.DateTimeField(auto_now_add=True)
    mesa = models.IntegerField()
    mesero = models.IntegerField()
    codigoEstado = models.IntegerField()
    productos = models.CharField(max_length=100)
    notas = models.TextField(max_length=100)
    total = models.IntegerField()

    def __str__(self):
        return self.numeroOrden
    
    class Meta:
        db_table = 'orden'