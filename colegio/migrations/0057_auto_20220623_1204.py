# Generated by Django 3.2.8 on 2022-06-23 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colegio', '0056_alter_alumno_curso'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apoderado',
            name='estadoCivil',
        ),
        migrations.RemoveField(
            model_name='apoderado',
            name='fechaNacimiento',
        ),
        migrations.RemoveField(
            model_name='apoderado',
            name='lugarTrabajo',
        ),
        migrations.RemoveField(
            model_name='apoderado',
            name='nivel',
        ),
        migrations.RemoveField(
            model_name='apoderado',
            name='profesion',
        ),
        migrations.AddField(
            model_name='padre',
            name='alumno',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='colegio.alumno'),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='hermanos',
            field=models.CharField(blank=True, default='No', max_length=200),
        ),
        migrations.AlterField(
            model_name='apoderado',
            name='email',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
