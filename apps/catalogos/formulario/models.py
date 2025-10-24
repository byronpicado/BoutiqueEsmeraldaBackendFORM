from django.db import models


class Formulario(models.Model):
    Nombre = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Mensaje = models.CharField(max_length=100)
    FechaRegistro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Formulario'

    def __str__(self):
        return f"{self.Nombre}"


