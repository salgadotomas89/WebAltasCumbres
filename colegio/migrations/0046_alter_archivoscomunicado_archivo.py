# Generated by Django 3.2.8 on 2022-05-05 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colegio', '0045_auto_20220505_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivoscomunicado',
            name='archivo',
            field=models.FileField(blank=True, null=True, upload_to='comunicados'),
        ),
    ]
