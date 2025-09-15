from django.contrib import admin
from .models import Avance

@admin.register(Avance)
class AvanceAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'materia', 'aprobado', 'fecha_aprobacion')
    list_filter = ('aprobado', 'materia', 'estudiante')
    search_fields = ('estudiante__user__username', 'materia__nombre')
