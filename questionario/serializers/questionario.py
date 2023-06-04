from rest_framework import serializers
from questionario.models.questionario import Questionario

class QuestionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionario
        fields = '__all__'
