from django.contrib import admin

from django.contrib import admin
from .models import Materia

@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    list_filter = ('carreras',)
    search_fields = ('codigo', 'nombre')