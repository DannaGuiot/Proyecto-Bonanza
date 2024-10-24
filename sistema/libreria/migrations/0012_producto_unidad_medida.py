# Generated by Django 4.1.3 on 2024-07-24 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0011_remove_producto_unidad_medida'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='unidad_medida',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='productos', to='libreria.unidadmedida', verbose_name='UnidadMedida'),
        ),
    ]
