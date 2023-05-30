from rest_framework import serializers
from sucursal.models.sucursal import Sucursal
from ..models import Redes
from .sucursal import SucursalSerializer


class RedesSerializer(serializers.ModelSerializer):
    sucursal = SucursalSerializer()

    class Meta:
        model = Redes
        fields = ['sucursal', 'red_name', 'fecha', 'cantidad']

    def create(self, validated_data):
        sucursal_data = validated_data.pop('sucursal')
        sucursal = Sucursal.objects.create(**sucursal_data)
        redes = Redes.objects.create(sucursal=sucursal, **validated_data)
        return redes
