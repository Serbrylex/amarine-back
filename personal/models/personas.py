from django.db import models
from django.contrib.auth.models import User
from sucursal.models.sucursal import Sucursal

class Personal(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    # Otros campos del personal

    def __str__(self):
        return self.usuario.username
