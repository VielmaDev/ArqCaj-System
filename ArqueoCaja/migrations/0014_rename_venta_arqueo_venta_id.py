# Generated by Django 3.2.9 on 2023-06-20 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ArqueoCaja', '0013_rename_venta_id_arqueo_venta'),
    ]

    operations = [
        migrations.RenameField(
            model_name='arqueo',
            old_name='venta',
            new_name='venta_id',
        ),
    ]
