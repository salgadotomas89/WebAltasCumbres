# Generated by Django 3.2.8 on 2022-04-11 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colegio', '0021_alter_curso_profesorjefe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colegio.curso'),
        ),
    ]
