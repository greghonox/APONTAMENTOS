# Generated by Django 4.0 on 2022-05-03 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_funcionariouser_alter_holerite_id_user_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FuncionarioUser',
            new_name='Funcionario',
        ),
    ]
