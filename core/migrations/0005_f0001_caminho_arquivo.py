# Generated by Django 4.0.4 on 2022-05-01 00:45

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_f0001_caminho_arquivo'),
    ]

    operations = [
        migrations.AddField(
            model_name='f0001',
            name='caminho_arquivo',
            field=models.FileField(default=1, upload_to=core.models.caminho_upload),
            preserve_default=False,
        ),
    ]