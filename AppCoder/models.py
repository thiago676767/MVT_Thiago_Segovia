from django.db import models

class Familia(models.Model):

    nombre = models.CharField(max_length=10)
    parentesco = models.CharField(max_length=10)
    fecha = models.DateTimeField("Fecha")
    edad = models.IntegerField("Edad")