# Generated by Django 3.2.8 on 2022-03-03 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colegio', '0022_alter_noticia_documento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='documento',
            field=models.ImageField(upload_to='noticias'),
        ),
    ]