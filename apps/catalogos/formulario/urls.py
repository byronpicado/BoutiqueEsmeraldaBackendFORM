from django.urls import path
from .views import FormularioApiView

app_name = 'formulario'

urlpatterns = [
    # Endpoint raíz de la app: se puede acceder con /api/contacto/ si lo incluyes así en config/urls.py
    path('', FormularioApiView.as_view(), name='api_formulario'),
]
