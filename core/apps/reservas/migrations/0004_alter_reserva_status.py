# Generated by Django 5.0.3 on 2024-03-22 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0003_alter_reserva_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='status',
            field=models.CharField(choices=[('confirmada', 'Confirmada'), ('cancelada', 'Cancelada'), ('concluida', 'Concluída')], default='confirmada', max_length=10),
        ),
    ]
