# Generated by Django 5.0.3 on 2024-03-20 14:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hoteis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField()),
                ('data_termino', models.DateField()),
                ('status', models.CharField(max_length=50)),
                ('quarto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservas', to='hoteis.quarto')),
            ],
        ),
    ]
