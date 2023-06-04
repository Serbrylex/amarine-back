from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated

from .models.questionario import Questionario
from .models.respuestas import Respuestas
from .models.preguntas import Preguntas
from personal.models.personas import Personal
from questionario.models.user_respuestas import UserRespuestas

from .serializers.questionario import QuestionarioSerializer
from .serializers.preguntas import PreguntasSerializer
from .serializers.respuestas import RespuestasSerializer


class QuestionarioView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        questionario = Questionario.objects.filter(pk=id)

        if len(questionario) == 0:
            return Response({'detail': 'No se encontraron datos'}, status=status.HTTP_404_NOT_FOUND)
        
        data = {
            'questionario': {
                'nombre': questionario[0].nombre,
                'pk': questionario[0].pk
            },
            'preguntas': []
        }
        preguntas = Preguntas.objects.filter(questionario=questionario[0])

        for pregunta in preguntas:
            respuestas = Respuestas.objects.filter(pregunta=pregunta).order_by('porcentaje')

            serializer = RespuestasSerializer(data=respuestas, many=True)
            serializer.is_valid()

            data['preguntas'].append({
                'pregunta': pregunta.pregunta,
                'pk': pregunta.pk,
                'respuestas': serializer.data
            })
        
        return Response(data, status=status.HTTP_200_OK)


class ValidarQuestionario(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, id):

        # Acá va lógica perronaajsd flkashflkashfkasjhksejhf

        respuestas = request.data
        resultado = 0

        questionario = Questionario.objects.get(pk=id)

        res = Respuestas.objects.filter(questionario=questionario)

        valor_pregunta = 100 / len(respuestas)

        for x in respuestas:
            resp_referencia = res.filter(pk=x)
            resultado += (valor_pregunta / 100) * resp_referencia[0].porcentaje
            personal = Personal.objects.get(usuario=request.user)
            UserRespuestas.objects.create(
                questionario=questionario, respuesta=resp_referencia[0], personal=personal
            )

        data = {
            'resultado': resultado
        }
        return Response(data, status=status.HTTP_200_OK)
