# Generated by Django 5.0.7 on 2024-08-14 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0028_compra_activado_persona_activado_venta_activado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='estado',
        ),
    ]
