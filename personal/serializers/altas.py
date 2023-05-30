from rest_framework import serializers
from sucursal.models.sucursal import Sucursal
from personal.models.personas import Personal
from ..models import AltaPersonal
from .personas import PersonalSerializer
from sucursal.serializers.sucursal import SucursalSerializer

class AltaPersonalSerializer(serializers.ModelSerializer):
    personal = PersonalSerializer()
    sucursal = SucursalSerializer()

    class Meta:
        model = AltaPersonal
        fields = ['personal', 'sucursal', 'fecha']

    def create(self, validated_data):
        personal_data = validated_data.pop('personal')
        sucursal_data = validated_data.pop('sucursal')
        personal = Personal.objects.create(**personal_data)
        sucursal = Sucursal.objects.create(**sucursal_data)
        alta_personal = AltaPersonal.objects.create(personal=personal, sucursal=sucursal, **validated_data)
        return alta_personal
