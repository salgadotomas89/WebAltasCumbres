# Generated by Django 3.0.1 on 2023-03-27 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colegio', '0076_taller'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taller',
            old_name='alumno',
            new_name='profesor',
        ),
        migrations.RemoveField(
            model_name='taller',
            name='curso',
        ),
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alumno', models.CharField(max_length=100)),
                ('curso', models.CharField(max_length=100)),
                ('taller', models.ManyToManyField(to='colegio.Taller')),
            ],
        ),
    ]