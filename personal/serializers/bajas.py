from rest_framework import serializers
from sucursal.models.sucursal import Sucursal
from personal.models.personas import Personal

from personal.models.bajas import BajaPersonal

from .personas import PersonalSerializer
from sucursal.serializers.sucursal import SucursalSerializer


class BajaPersonalSerializer(serializers.ModelSerializer):
    personal = PersonalSerializer()
    sucursal = SucursalSerializer()

    class Meta:
        model = BajaPersonal
        fields = ['personal', 'sucursal', 'motivo', 'fecha']

    def create(self, validated_data):
        personal_data = validated_data.pop('personal')
        sucursal_data = validated_data.pop('sucursal')
        personal = Personal.objects.create(**personal_data)
        sucursal = Sucursal.objects.create(**sucursal_data)
        baja_personal = BajaPersonal.objects.create(personal=personal, sucursal=sucursal, **validated_data)
        return baja_personal
