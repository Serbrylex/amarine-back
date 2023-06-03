from django.db import models
from sucursal.models.sucursal import Sucursal
from personal.models.personas import Personal
from django.utils import timezone

class AltaPersonal(models.Model):
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    fecha = models.DateField(default=timezone.now())

    def __str__(self):
        return f"Alta de {self.personal} en {self.sucursal}"
