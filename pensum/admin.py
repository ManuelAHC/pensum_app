from django.contrib import admin

from django.contrib import admin
from .models import Pensum

@admin.register(Pensum)
class PensumAdmin(admin.ModelAdmin):
    list_display = ('carrera', 'materia', 'semestre', 'es_electiva')
    list_filter = ('carrera', 'semestre', 'es_electiva')
    search_fields = ('carrera__nombre', 'materia__nombre')