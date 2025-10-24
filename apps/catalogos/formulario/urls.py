from django.urls import path
from .views import FormularioApiView

app_name = 'formulario'

urlpatterns = [
    path('', FormularioApiView.as_view(), name='api_formulario'),
]
