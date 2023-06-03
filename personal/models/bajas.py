from django.db import models
from sucursal.models.sucursal import Sucursal
from personal.models.personas import Personal
from datetime import datetime

class BajaPersonal(models.Model):
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    motivo_choices = [
        ('voluntaria', 'Voluntaria'),
        ('abandono', 'Abandono')
    ]
    motivo = models.CharField(max_length=20, choices=motivo_choices)
    fecha = models.DateField(default=datetime.now())

    def __str__(self):
        return f"Baja de {self.personal} en {self.sucursal}"
