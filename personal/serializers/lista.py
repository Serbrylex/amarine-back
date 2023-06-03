from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from personal.models.personas import Personal, User
from personal.models.lista import PaseLista
from .personas import PersonalSerializer


class PaseListaCreateSerializer(serializers.Serializer):

    email = serializers.EmailField()
    asistio = serializers.BooleanField()
    fecha = serializers.DateField()

    def validate(self, data):
        print(data)
        email = data['email']
        persona = Personal.objects.filter(usuario__email=email)
        if len(persona) == 0:
            raise serializers.ValidationError("Email doesn't match")
        
        self.context['persona'] = persona[0]
        return data


    def create(self, validated_data):
        personal_data = validated_data.pop('email')
        pase_lista = PaseLista.objects.create(personal=self.context['persona'], **validated_data)
        return pase_lista

class PaseListaSerializer(serializers.ModelSerializer):
    personal = PersonalSerializer()

    class Meta:
        model = PaseLista
        fields = ['personal', 'asistio', 'fecha']