# Generated by Django 3.2.8 on 2021-11-11 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colegio', '0007_alter_noticia_documento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='img',
        ),
    ]
