# Generated by Django 4.2.4 on 2023-12-22 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ingresos', '0002_ventas_procesado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ventas',
            name='tasa_id',
        ),
    ]
