# Generated by Django 3.0.1 on 2023-03-28 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colegio', '0077_auto_20230327_1300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscripcion',
            name='taller',
        ),
        migrations.AddField(
            model_name='inscripcion',
            name='taller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='colegio.Taller'),
        ),
    ]
