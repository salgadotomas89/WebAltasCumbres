# Generated by Django 3.2.8 on 2022-05-03 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colegio', '0039_noticia_noticia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='noticia',
        ),
    ]