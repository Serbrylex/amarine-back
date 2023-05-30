from rest_framework import serializers
from ..models import Questionario

class QuestionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionario
        fields = ['nombre']
