# Generated by Django 3.2.8 on 2021-11-22 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colegio', '0018_profesor_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesor',
            name='universidad',
            field=models.CharField(default='sin', max_length=100),
            preserve_default=False,
        ),
    ]
