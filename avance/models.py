from django.db import models

class Avance(models.Model):
    estudiante = models.ForeignKey('usuarios.Estudiante', on_delete=models.CASCADE)
    materia = models.ForeignKey('materias.Materia', on_delete=models.CASCADE)
    aprobado = models.BooleanField(default=False)
    fecha_aprobacion = models.DateField(null=True, blank=True)

    class Meta:
        unique_together = ('estudiante', 'materia')

    def __str__(self):
        return f"{self.estudiante} - {self.materia} ({'Aprobada' if self.aprobado else 'Pendiente'})"
