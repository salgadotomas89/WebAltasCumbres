# Generated by Django 3.0.1 on 2023-04-02 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colegio', '0081_auto_20230330_1830'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tenista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('curso', models.CharField(max_length=100)),
                ('puntaje', models.IntegerField(blank=True, default=0)),
                ('ganados', models.IntegerField(blank=True, default=0)),
                ('perdidos', models.IntegerField(blank=True, default=0)),
                ('partidos', models.IntegerField(blank=True, default=0)),
            ],
        ),
    ]
