# Generated by Django 3.2.9 on 2023-06-21 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ingresos', '0001_initial'),
        ('Inventario', '0013_auto_20230620_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario_ventas',
            name='venta_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Ingresos.ventas'),
        ),
    ]
