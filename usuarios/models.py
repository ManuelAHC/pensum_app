from django.db import models
from django.contrib.auth.models import User

class Estudiante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    carrera = models.ForeignKey('carreras.Carrera', on_delete=models.SET_NULL, null=True)
    ingreso = models.PositiveIntegerField(help_text="Año de ingreso")

    def __str__(self):
        return self.user.get_full_name()
