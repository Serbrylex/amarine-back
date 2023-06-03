from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from .models.personas import Personal
from .models.altas import AltaPersonal
from .models.bajas import BajaPersonal

from .serializers.personas import PersonalSerializer, UserSerializer
from .serializers.lista import PaseListaSerializer, PaseListaCreateSerializer
from .serializers.altas import AltaPersonalSerializer
from .serializers.bajas import BajaPersonalSerializer

class LoginView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        if 'email' in request.data and 'password' in request.data:
            email = request.data['email']
            password = request.data['password']
            
            # Autenticar al usuario
            user = authenticate(request, email=email, password=password)

            if user is not None:
                # El usuario se autenticó correctamente
                
                personal = Personal.objects.get(usuario=user)
                token, _ = Token.objects.get_or_create(user=user)
                data = {
                    'state': True,
                    'detail': 'Inicio de sesión exitoso',
                    'usuario': PersonalSerializer(personal).data,
                    'token': token.key
                }
                return Response(data, status=status.HTTP_200_OK)
            else:
                # El usuario no se pudo autenticar
                return Response({'detail': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            # Los datos de entrada no son válidos
            return Response({'detail': 'Wrong data'}, status=status.HTTP_400_BAD_REQUEST)
        

class SendListaView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PaseListaCreateSerializer(data=request.data, many=True)
        if serializer.is_valid():
            data = serializer.save()
            res = PaseListaSerializer(data=data, many=True)
            res.is_valid()
            return Response(res.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonalListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, email=None):
        if (email):
            personal = Personal.objects.filter(usuario__email=email) 
        else:
            personal = Personal.objects.all()

        if len(personal) == 0:
            return Response({'detail': 'No se encontraron datos'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PersonalSerializer(personal, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class BajaListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        bajas = BajaPersonal.objects.all()

        if len(bajas) == 0:
            return Response({'detail': 'No se encontraron datos'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = BajaPersonalSerializer(bajas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class AltaListView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        altas = AltaPersonal.objects.all()

        if len(altas) == 0:
            return Response({'detail': 'No se encontraron datos'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AltaPersonalSerializer(altas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)