# Generated by Django 3.2.8 on 2022-03-28 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colegio', '0006_auto_20220324_1046'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asistente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('profesion', models.CharField(default='asistente de la educación', max_length=100)),
                ('ciclo', models.IntegerField(default=4)),
                ('universidad', models.CharField(default='-', max_length=100)),
                ('correo', models.CharField(default='sin correo', max_length=200)),
                ('foto', models.ImageField(upload_to='asistentes')),
            ],
        ),
        migrations.AddField(
            model_name='guia',
            name='estado',
            field=models.CharField(default='por imprimir', max_length=100),
        ),
    ]
