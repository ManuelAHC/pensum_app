from django.db import models

class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)
    descripcion = models.TextField(blank=True)
    carreras = models.ManyToManyField('carreras.Carrera', related_name='materias', blank=True)

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"