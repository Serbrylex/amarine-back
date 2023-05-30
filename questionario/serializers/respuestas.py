from rest_framework import serializers
from ..models import Respuestas
from questionario.models import Questionario
from .questionario import QuestionarioSerializer


class RespuestasSerializer(serializers.ModelSerializer):
    questionario = QuestionarioSerializer()

    class Meta:
        model = Respuestas
        fields = ['questionario', 'respuesta', 'porcentaje']

    def create(self, validated_data):
        questionario_data = validated_data.pop('questionario')
        questionario = Questionario.objects.create(**questionario_data)
        respuestas = Respuestas.objects.create(questionario=questionario, **validated_data)
        return respuestas
