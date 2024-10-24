# Generated by Django 5.0.7 on 2024-08-06 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0019_marca_estado_presentacion_estado_producto_estado_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presentacion',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='marca',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='unidadmedida',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='categoria',
            name='estado',
        ),
        migrations.DeleteModel(
            name='Estado',
        ),
    ]
