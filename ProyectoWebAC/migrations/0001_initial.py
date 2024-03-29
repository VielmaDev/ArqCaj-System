# Generated by Django 3.2.9 on 2023-05-26 08:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='tasa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dolar', models.CharField(max_length=4)),
                ('Euro', models.CharField(max_length=4)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Divisa',
                'verbose_name_plural': 'Divisas',
            },
        ),
        migrations.CreateModel(
            name='tienda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon', models.CharField(max_length=30)),
                ('rif', models.CharField(max_length=12)),
                ('direccion', models.CharField(max_length=25)),
                ('telf', models.CharField(max_length=30, null=True)),
                ('redes', models.CharField(max_length=25, null=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now_add=True)),
                ('usuario_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Tienda',
                'verbose_name_plural': 'Tiendas',
            },
        ),
        migrations.CreateModel(
            name='caja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_caja', models.CharField(default='', max_length=4)),
                ('created', models.DateField(auto_now_add=True)),
                ('update', models.DateField(auto_now_add=True)),
                ('tienda_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ProyectoWebAC.tienda')),
            ],
            options={
                'verbose_name': 'Caja',
                'verbose_name_plural': 'Cajas',
            },
        ),
    ]
