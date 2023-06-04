from rest_framework import serializers
from questionario.models.respuestas import Respuestas
from questionario.models.questionario import Questionario
from .questionario import QuestionarioSerializer


class RespuestasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Respuestas
        fields = ['pk', 'respuesta', 'porcentaje']

    def create(self, validated_data):
        questionario_data = validated_data.pop('questionario')
        questionario = Questionario.objects.create(**questionario_data)
        respuestas = Respuestas.objects.create(questionario=questionario, **validated_data)
        return respuestas
