# Generated by Django 4.2.4 on 2024-01-29 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoWebAC', '0015_tasadivisa_delete_tasadolar'),
        ('Ingresos', '0005_remove_ventas_tasadolar'),
    ]

    operations = [
        migrations.AddField(
            model_name='ventas',
            name='tasaDivisa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ProyectoWebAC.tasadivisa'),
            preserve_default=False,
        ),
    ]
