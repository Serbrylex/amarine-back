from django.db import models
from personal.models.personas import Personal

class PaseLista(models.Model):
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE)
    asistio = models.BooleanField()
    fecha = models.DateField()

    def __str__(self):
        return f"Pase de lista de {self.personal} el {self.fecha}"
