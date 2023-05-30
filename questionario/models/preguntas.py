from django.db import models
from questionario.models.questionario import Questionario

class Preguntas(models.Model):
    questionario = models.ForeignKey(Questionario, on_delete=models.CASCADE)
    pregunta = models.TextField()

    def __str__(self):
        return self.pregunta
