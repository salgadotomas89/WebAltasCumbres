# Generated by Django 3.2.8 on 2022-04-21 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colegio', '0032_auto_20220421_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='edad',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='puebloOriginario',
            field=models.BooleanField(blank=True, default='no'),
        ),
    ]