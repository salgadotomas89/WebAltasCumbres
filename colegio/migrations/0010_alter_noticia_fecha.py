# Generated by Django 3.2.8 on 2021-11-17 01:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('colegio', '0009_noticia_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
