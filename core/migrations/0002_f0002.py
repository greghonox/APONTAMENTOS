# Generated by Django 4.0.4 on 2022-04-24 16:24

import core.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='F0002',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_insercao', models.DateTimeField(auto_now_add=True, verbose_name='Data de Registro')),
                ('data_modificacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de Modificação')),
                ('modalidade', models.CharField(choices=[('HOL', 'Holerite'), ('PONT', 'Ponto')], default='HOL', max_length=4)),
                ('mes', models.IntegerField()),
                ('ano', models.IntegerField()),
                ('caminho_arquivo', models.FileField(upload_to=core.models.caminho_upload)),
                ('nome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.funcionario')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
