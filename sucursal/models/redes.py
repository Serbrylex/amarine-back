from django.db import models
from sucursal.models.sucursal import Sucursal

class Redes(models.Model):
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    red_name = models.CharField(max_length=100)
    fecha = models.DateField()
    cantidad = models.IntegerField()

    def __str__(self):
        return self.red_name
