from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ClienteRegistrationSerializer


class ClienteRegistrationView(APIView):
    permission_classes = [AllowAny, ]

    @swagger_auto_schema(request_body=ClienteRegistrationSerializer)
    def post(self, request, *args, **kwargs):
        serializer = ClienteRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            cliente = serializer.save()
            return Response({
                'username': cliente.username,
                'email': cliente.email,
                'cpf': cliente.cpf
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
