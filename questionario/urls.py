from django.urls import path
from .views import QuestionarioView


urlpatterns = [
    # Agrega la URL para obtener todos los datos de Personal
    path('<int:id>/', QuestionarioView.as_view(), name='quetionario-view'),
]
