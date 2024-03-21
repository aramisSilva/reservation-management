from django.contrib.auth.models import User, Group
from rest_framework import serializers


class AdminUserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        admin_group = Group.objects.get(name='administradores')
        user.groups.add(admin_group)
        return user


class EmployeeRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        employee_group = Group.objects.get(name='funcionários')
        user.groups.add(employee_group)
        return user