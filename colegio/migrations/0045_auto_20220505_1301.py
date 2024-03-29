# Generated by Django 3.2.8 on 2022-05-05 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colegio', '0044_comunicado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comunicado',
            name='archivos',
        ),
        migrations.CreateModel(
            name='ArchivosComunicado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archivo', models.ImageField(blank=True, null=True, upload_to='comunicados')),
                ('comunicado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colegio.comunicado')),
            ],
        ),
    ]
