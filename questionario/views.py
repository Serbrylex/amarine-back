from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate

from .models.questionario import Questionario

from .serializers.questionario import QuestionarioSerializer


class QuestionarioView(APIView):
    def get(self, request, id):
        questionario = Questionario.objects.filter(pk=id)

        if len(questionario) == 0:
            return Response({'detail': 'No se encontraron datos'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = BajaPersonalSerializer(questionario[0])
        return Response(serializer.data, status=status.HTTP_200_OK)


class ValidarQuestionario(APIView):
    def post(self, request):

        # Acá va lógica perronaajsd flkashflkashfkasjhksejhf

        serializer = PaseListaSerializer(data=request.data, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
