from django.db import models

class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    latitud = models.FloatField()
    longitud = models.FloatField()
    # Otros campos de la sucursal

    def __str__(self):
        return self.nombre