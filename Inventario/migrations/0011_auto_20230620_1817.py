# Generated by Django 3.2.9 on 2023-06-20 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ArqueoCaja', '0016_alter_arqueo_procesado'),
        ('ProyectoWebAC', '0004_auto_20230530_2358'),
        ('Inventario', '0010_auto_20230619_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario_ventas',
            name='arqueo_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ArqueoCaja.arqueo'),
        ),
        migrations.AlterField(
            model_name='inventario_ventas',
            name='procesado',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='inventario_ventas',
            name='tienda_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProyectoWebAC.tienda'),
        ),
    ]
