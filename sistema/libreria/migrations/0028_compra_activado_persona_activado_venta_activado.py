# Generated by Django 5.0.7 on 2024-08-14 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0027_compra_persona_venta'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='activado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='activado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='venta',
            name='activado',
            field=models.BooleanField(default=True),
        ),
    ]
