from rest_framework import serializers
from .models import Formulario

class FormularioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formulario
        fields = '__all__'
        read_only_fields = ('FechaRegistro',)
