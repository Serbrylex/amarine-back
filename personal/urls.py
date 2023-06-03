from django.urls import path
from .views import (
    LoginView, PersonalListView, SendListaView,BajaListView, AltaListView
)


urlpatterns = [
    # Agrega la URL para obtener todos los datos de Personal
    path('login/', LoginView.as_view(), name='login'),
    path('personal/', PersonalListView.as_view(), name='personal-list'),
    path('personal/send-lista/', SendListaView.as_view(), name='personal-send-list'),

    path('personal/bajas/', BajaListView.as_view(), name='personal-bajas-list'),
    path('personal/altas/', AltaListView.as_view(), name='personal-altas-list'),
    
    path('personal/<str:email>/', PersonalListView.as_view(), name='persona'),
]
