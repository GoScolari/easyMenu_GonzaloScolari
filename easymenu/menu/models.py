from django.db import models

class Orden(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    hora = models.TimeField()
    mesa = models.IntegerField()
    estado = models.CharField(max_length=100)
    productos = models.JSONField()
    notas = models.TextField()
