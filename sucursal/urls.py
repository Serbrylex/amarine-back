from django.urls import path
from .views import SucursalView, RedesView


urlpatterns = [
    # Agrega la URL para obtener todos los datos de Personal
    path('', SucursalView.as_view(), name='all-sucursals-view'),
    path('redes/', RedesView.as_view(), name='all-redes-view'),
    path('redes/<int:id>/', RedesView.as_view(), name='red-view'),
    path('<int:id>/', SucursalView.as_view(), name='sucursal-view'),
]
