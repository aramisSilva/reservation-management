from django.contrib.auth.models import User
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.views import APIView

from core.apps.clientes import permissions
from .serializers import AdminUserRegistrationSerializer, EmployeeRegistrationSerializer
from drf_yasg.utils import swagger_auto_schema

class UserRegistrationView(APIView):
    permission_classes = [permissions.IsSuperUser]

    @swagger_auto_schema(request_body=AdminUserRegistrationSerializer)
    def post(self, request, *args, **kwargs):
        serializer = AdminUserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateEmployeeView(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    @swagger_auto_schema(request_body=EmployeeRegistrationSerializer)
    def post(self, request, *args, **kwargs):
        if not request.user.groups.filter(name='administradores').exists():
            return Response({"detail": "Apenas administradores podem criar funcionários."},
                            status=status.HTTP_403_FORBIDDEN)

        serializer = EmployeeRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)