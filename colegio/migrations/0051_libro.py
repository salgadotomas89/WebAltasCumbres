# Generated by Django 3.2.8 on 2022-06-01 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colegio', '0050_alter_comunicado_texto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('autor', models.TextField()),
                ('isbn', models.TextField()),
                ('editorial', models.TextField()),
                ('resumen', models.TextField()),
                ('foto', models.ImageField(upload_to='libros')),
            ],
        ),
    ]
