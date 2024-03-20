from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser
from validate_docbr import CPF


def validar_cpf(value):
    cpf = CPF()
    if not cpf.validate(value):
        raise ValidationError(f'{value} não é um CPF válido.')


class Cliente(AbstractUser):
    cpf = models.CharField('CPF', max_length=14, unique=True, validators=[validar_cpf],
                           help_text='Informe o CPF no formato XXX.XXX.XXX-XX.')
