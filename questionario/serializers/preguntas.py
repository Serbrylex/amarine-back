from rest_framework import serializers
from questionario.models.questionario import Questionario
from questionario.models.preguntas import Preguntas
from .questionario import QuestionarioSerializer


class PreguntasSerializer(serializers.ModelSerializer):
    questionario = QuestionarioSerializer()

    class Meta:
        model = Preguntas
        fields = ['pregunta']

    def create(self, validated_data):
        questionario_data = validated_data.pop('questionario')
        questionario = Questionario.objects.create(**questionario_data)
        pregunta = Preguntas.objects.create(questionario=questionario, **validated_data)
        return pregunta
