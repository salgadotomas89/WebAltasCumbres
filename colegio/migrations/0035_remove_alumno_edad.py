# Generated by Django 3.2.8 on 2022-04-21 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colegio', '0034_alter_alumno_edad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='edad',
        ),
    ]