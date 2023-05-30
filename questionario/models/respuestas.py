from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Respuestas(models.Model):
    questionario = models.ForeignKey('Questionario', on_delete=models.CASCADE)
    respuesta = models.TextField()
    porcentaje = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return self.respuesta
