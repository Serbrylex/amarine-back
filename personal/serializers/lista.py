from rest_framework import serializers
from personal.models.personas import Personal
from ..models import PaseLista
from .personas import PersonalSerializer


class PaseListaSerializer(serializers.ModelSerializer):
    personal = PersonalSerializer()

    class Meta:
        model = PaseLista
        fields = ['personal', 'asistio', 'fecha']

    def create(self, validated_data):
        personal_data = validated_data.pop('personal')
        personal = Personal.objects.create(**personal_data)
        pase_lista = PaseLista.objects.create(personal=personal, **validated_data)
        return pase_lista
