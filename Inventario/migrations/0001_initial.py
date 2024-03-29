# Generated by Django 3.2.9 on 2023-05-26 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ProyectoWebAC', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='inventario_ventas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calzados', models.CharField(max_length=5)),
                ('ropa', models.CharField(max_length=5)),
                ('accesorios', models.CharField(max_length=5)),
                ('piezas', models.CharField(max_length=10)),
                ('procesado', models.BooleanField(default=False)),
                ('created', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now_add=True)),
                ('tienda_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ProyectoWebAC.tienda')),
            ],
            options={
                'verbose_name': 'Inventario',
                'verbose_name_plural': 'Inventarios',
            },
        ),
    ]
