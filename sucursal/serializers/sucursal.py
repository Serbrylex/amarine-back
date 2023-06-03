from rest_framework import serializers
from sucursal.models.sucursal import Sucursal

class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = ['nombre', 'latitud', 'longitud']
