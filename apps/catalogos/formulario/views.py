from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.catalogos.formulario.models import Formulario
from .serializers import FormularioSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny

class FormularioApiView(APIView):
    permission_classes = [AllowAny]

    model = Formulario  # Aquí definimos el modelo explícitamente
    @swagger_auto_schema(request_body=FormularioSerializer, responses={200: FormularioSerializer})
    def post(self, request):
        serializer = FormularioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
