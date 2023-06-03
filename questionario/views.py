from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated

from .models.questionario import Questionario
from .models.respuestas import Respuestas
from questionario.models.user_respuestas import UserRespuestas

from .serializers.questionario import QuestionarioSerializer


class QuestionarioView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        questionario = Questionario.objects.filter(pk=id)

        if len(questionario) == 0:
            return Response({'detail': 'No se encontraron datos'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = QuestionarioSerializer(questionario[0])
        return Response(serializer.data, status=status.HTTP_200_OK)


class ValidarQuestionario(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):

        # Acá va lógica perronaajsd flkashflkashfkasjhksejhf

        respuestas = request.data
        resultado = 0

        res = Respuestas.objects.filter(questionario__pk=pk)

        for x in respuestas:
            resp_referencia = res.filter(pk=x)
            resultado += resp_referencia.porcentaje / 100 
            UserRespuestas.objects.create(questionario=pk, respuesta=resp_referencia, personal=request.user)


        serializer = QuestionarioSerializer(data=request.data, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
