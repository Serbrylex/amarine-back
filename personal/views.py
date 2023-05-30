from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate

from .models.personas import Personal
from .models.altas import AltaPersonal
from .models.bajas import BajaPersonal

from .serializers.personas import PersonalSerializer
from .serializers.lista import PaseListaSerializer
from .serializers.altas import AltaPersonalSerializer
from .serializers.bajas import BajaPersonalSerializer

class LoginView(APIView):
    def post(self, request):
        serializer = PersonalSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data['usuario']['username']
            password = serializer.validated_data['usuario']['password']
            
            # Autenticar al usuario
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # El usuario se autenticó correctamente
                return Response({'detail': 'Inicio de sesión exitoso'}, status=status.HTTP_200_OK)
            else:
                # El usuario no se pudo autenticar
                return Response({'detail': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            # Los datos de entrada no son válidos
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class SendListaView(APIView):
    def post(self, request):
        serializer = PaseListaSerializer(data=request.data, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonalListView(APIView):
    def get(self, request, username=None):
        if (username):
            personal = Personal.objects.filter(usuario__username=username) 
        else:
            personal = Personal.objects.all()

        if len(personal) == 0:
            return Response({'detail': 'No se encontraron datos'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PersonalSerializer(personal, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class BajaListView(APIView):
    def get(self, request):
        bajas = BajaPersonal.objects.all()

        if len(bajas) == 0:
            return Response({'detail': 'No se encontraron datos'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = BajaPersonalSerializer(bajas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class AltaListView(APIView):
    def get(self, request):
        altas = AltaPersonal.objects.all()

        if len(altas) == 0:
            return Response({'detail': 'No se encontraron datos'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AltaPersonalSerializer(altas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)