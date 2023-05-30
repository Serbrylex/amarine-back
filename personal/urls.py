from django.urls import path
from .views import (
    LoginView, PersonalListView, SendListaView,BajaListView, AltaListView
)


urlpatterns = [
    # Agrega la URL para obtener todos los datos de Personal
    path('login/', LoginView.as_view(), name='login'),
    path('personal/', PersonalListView.as_view(), name='personal-list'),
    path('personal/send-lista/', SendListaView.as_view(), name='personal-list'),

    path('personal/bajas/', BajaListView.as_view(), name='personal-list'),
    path('personal/altas/', AltaListView.as_view(), name='personal-list'),
    
    path('personal/<str:username>/', PersonalListView.as_view(), name='personal-list'),
]
