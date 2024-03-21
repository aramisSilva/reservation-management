from django.contrib.auth.models import Group
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import Cliente


class ClienteRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('username', 'email', 'cpf', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.pop('password'))
        cliente = Cliente.objects.create(**validated_data)
        grupo_clientes = Group.objects.get(name='Clientes')
        cliente.groups.add(grupo_clientes)
        cliente.save()
        return cliente
