# Generated by Django 3.0.1 on 2023-04-03 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colegio', '0082_tenista'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tenista',
            name='partidos',
        ),
        migrations.AddField(
            model_name='tenista',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='tenistas'),
        ),
    ]