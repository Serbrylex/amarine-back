from django.db import models

from personal.models.personas import Personal

class UserRespuestas(models.Model):
    questionario = models.ForeignKey('Questionario', on_delete=models.CASCADE)
    respuesta = models.ForeignKey('Respuestas', on_delete=models.CASCADE)
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE)

    def __str__(self):
        return self.respuesta
