# Generated by Django 3.2.9 on 2023-06-20 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ArqueoCaja', '0012_arqueo_venta_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='arqueo',
            old_name='venta_id',
            new_name='venta',
        ),
    ]
