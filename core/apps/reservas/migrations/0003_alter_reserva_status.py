# Generated by Django 5.0.3 on 2024-03-21 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0002_reserva_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='status',
            field=models.CharField(default='confirmada', max_length=10),
        ),
    ]
