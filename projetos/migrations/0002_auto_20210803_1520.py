# Generated by Django 3.2.5 on 2021-08-03 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prioridadetarefa',
            old_name='project',
            new_name='projeto',
        ),
        migrations.RenameField(
            model_name='tarefa',
            old_name='project',
            new_name='projeto',
        ),
        migrations.RenameField(
            model_name='tipotarefa',
            old_name='project',
            new_name='projeto',
        ),
    ]