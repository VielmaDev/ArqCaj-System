# Generated by Django 3.2.9 on 2023-06-06 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArqueoCaja', '0002_auto_20230530_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='arqueo',
            name='ft',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='arqueo',
            name='st',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]