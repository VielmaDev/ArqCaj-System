# Generated by Django 3.2.9 on 2023-06-17 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoWebAC', '0004_auto_20230530_2358'),
        ('ArqueoCaja', '0009_auto_20230612_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arqueo',
            name='caja_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProyectoWebAC.caja'),
        ),
        migrations.AlterField(
            model_name='arqueo',
            name='ingreso_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ArqueoCaja.ingresos'),
        ),
        migrations.AlterField(
            model_name='arqueo',
            name='tienda_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProyectoWebAC.tienda'),
        ),
        migrations.AlterField(
            model_name='ingresos',
            name='caja_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProyectoWebAC.caja'),
        ),
        migrations.AlterField(
            model_name='ingresos',
            name='tasa_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProyectoWebAC.tasa'),
        ),
        migrations.AlterField(
            model_name='ingresos',
            name='tienda_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProyectoWebAC.tienda'),
        ),
    ]
