# Generated by Django 3.2.8 on 2022-06-24 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colegio', '0067_auto_20220624_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='apoderado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='colegio.apoderado'),
        ),
    ]