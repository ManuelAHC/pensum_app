from django.db import models

class Pensum(models.Model):
    carrera = models.ForeignKey('carreras.Carrera', on_delete=models.CASCADE, related_name='pensums')
    materia = models.ForeignKey('materias.Materia', on_delete=models.CASCADE)
    semestre = models.PositiveIntegerField()
    es_electiva = models.BooleanField(default=False)

    class Meta:
        unique_together = ('carrera', 'materia')

    def __str__(self):
        return f"{self.carrera} - {self.materia} (Semestre {self.semestre})"
