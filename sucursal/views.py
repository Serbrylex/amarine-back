from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated

from sucursal.models.redes import Redes
from sucursal.models.sucursal import Sucursal

from .serializers.sucursal import SucursalSerializer
from .serializers.redes import RedesSerializer


class SucursalView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):

        if id:
            sucursal = Sucursal.objects.filter(pk=id)
        else:
            sucursal = Sucursal.objects.all()


        if len(sucursal) == 0:
            return Response({'detail': 'No se encontraron datos'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = SucursalSerializer(data=sucursal, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)


class RedesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):

        # Acá va lógica perronaajsd flkashflkashfkasjhksejhf

        if (id):
            redes = Redes.objects.filter(sucursal__pk=id) 
        else:
            redes = Redes.objects.all()

        if len(redes) == 0:
            return Response({'detail': 'No se encontraron datos'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = RedesSerializer(data=redes, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
