# Generated by Django 3.2.9 on 2023-06-20 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ArqueoCaja', '0014_rename_venta_arqueo_venta_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arqueo',
            name='venta_id',
        ),
    ]
