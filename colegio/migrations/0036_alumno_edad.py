# Generated by Django 3.2.8 on 2022-04-21 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colegio', '0035_remove_alumno_edad'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='edad',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
