from django.urls import path, include

urlpatterns = [
    path('formulario/', include('apps.catalogos.formulario.urls')),
]