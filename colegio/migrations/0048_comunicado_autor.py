# Generated by Django 3.2.8 on 2022-05-05 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colegio', '0047_rename_comunicado_comunicado_texto'),
    ]

    operations = [
        migrations.AddField(
            model_name='comunicado',
            name='autor',
            field=models.CharField(blank=True, default='Mauricio Orellana', max_length=100, null=True),
        ),
    ]
