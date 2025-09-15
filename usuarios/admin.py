from django.contrib import admin

from django.contrib import admin
from .models import Estudiante

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('user', 'carrera', 'ingreso')
    list_filter = ('carrera',)
    search_fields = ('user__username', 'user__first_name', 'user__last_name')