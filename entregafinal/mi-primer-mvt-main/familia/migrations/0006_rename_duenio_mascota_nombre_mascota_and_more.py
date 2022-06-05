# Generated by Django 4.0.5 on 2022-06-05 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familia', '0005_rename_nombre_alimento_nombre_alimento_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mascota',
            old_name='duenio',
            new_name='nombre_mascota',
        ),
        migrations.RemoveField(
            model_name='alimento',
            name='nombre_mascota',
        ),
        migrations.RemoveField(
            model_name='mascota',
            name='nombre',
        ),
        migrations.AlterField(
            model_name='persona',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
