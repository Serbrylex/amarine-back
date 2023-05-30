from rest_framework import serializers
from django.contrib.auth.models import User
from sucursal.models.sucursal import Sucursal
from personal.models.personas import Personal
from sucursal.serializers.sucursal import SucursalSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']  # Puedes incluir otros campos del modelo User si lo deseas

class PersonalSerializer(serializers.ModelSerializer):
    usuario = UserSerializer()
    sucursal = SucursalSerializer()

    class Meta:
        model = Personal
        fields = ['usuario', 'sucursal']  # Incluye otros campos del modelo Personal si lo deseas
