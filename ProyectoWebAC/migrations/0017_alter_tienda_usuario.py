# Generated by Django 3.2.9 on 2023-04-13 15:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ProyectoWebAC', '0016_tienda_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tienda',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
