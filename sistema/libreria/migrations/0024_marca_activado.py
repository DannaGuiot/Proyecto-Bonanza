# Generated by Django 5.0.7 on 2024-08-12 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0023_delete_libro'),
    ]

    operations = [
        migrations.AddField(
            model_name='marca',
            name='activado',
            field=models.BooleanField(default=True),
        ),
    ]
