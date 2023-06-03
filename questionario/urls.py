from django.urls import path
from .views import QuestionarioView, ValidarQuestionario


urlpatterns = [
    # Agrega la URL para obtener todos los datos de Personal
    path('<int:id>/', QuestionarioView.as_view(), name='quetionario-view'),
    path('<int:id>/validate/', ValidarQuestionario.as_view(), name='quetionario-view'),
]
