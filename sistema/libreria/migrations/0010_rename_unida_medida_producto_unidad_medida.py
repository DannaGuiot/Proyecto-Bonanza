# Generated by Django 4.1.3 on 2024-07-24 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0009_remove_producto_unidad_medida_producto_unida_medida_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='unida_medida',
            new_name='unidad_medida',
        ),
    ]