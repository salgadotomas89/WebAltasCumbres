# Generated by Django 3.2.8 on 2022-04-11 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colegio', '0023_alter_alumno_curso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='curso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='colegio.curso'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='profesorJefe',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='colegio.profesor'),
        ),
    ]