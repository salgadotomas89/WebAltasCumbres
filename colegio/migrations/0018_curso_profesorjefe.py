# Generated by Django 3.2.8 on 2022-04-11 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colegio', '0017_curso'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='profesorJefe',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='colegio.profesor'),
            preserve_default=False,
        ),
    ]
