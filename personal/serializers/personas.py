from rest_framework import serializers
from django.contrib.auth import get_user_model
from personal.models.personas import Personal
from sucursal.serializers.sucursal import SucursalSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'  # Puedes incluir otros campos del modelo User si lo deseas
        # exclude = ['password']


class PersonalSerializer(serializers.ModelSerializer):
    usuario = UserSerializer()
    sucursal = SucursalSerializer()

    class Meta:
        model = Personal
        fields = ['usuario', 'sucursal']  # Incluye otros campos del modelo Personal si lo deseas
