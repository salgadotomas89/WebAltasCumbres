# Generated by Django 3.0.1 on 2023-04-03 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colegio', '0083_auto_20230403_1308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tenista',
            name='image',
        ),
    ]