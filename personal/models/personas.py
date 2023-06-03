from django.db import models

from django.core.validators import RegexValidator

from django.contrib.auth.models import AbstractUser
from sucursal.models.sucursal import Sucursal

class User(AbstractUser):
    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        """Return username."""
        return self.username

class Personal(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    # Otros campos del personal

    def __str__(self):
        return self.usuario.username
