from django.contrib import admin
from .models import Formulario


@admin.register(Formulario)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('Nombre', 'Email', 'FechaRegistro')
    search_fields = ('Nombre', 'Email')
    list_filter = ('Email', 'FechaRegistro')

