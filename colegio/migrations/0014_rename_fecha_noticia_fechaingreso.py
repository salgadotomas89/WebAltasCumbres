# Generated by Django 3.2.8 on 2021-11-17 01:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colegio', '0013_noticia_fecha'),
    ]

    operations = [
        migrations.RenameField(
            model_name='noticia',
            old_name='fecha',
            new_name='fechaIngreso',
        ),
    ]
