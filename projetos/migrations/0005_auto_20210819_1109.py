# Generated by Django 3.2.5 on 2021-08-19 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0004_auto_20210817_1136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarefa',
            name='projeto',
        ),
        migrations.RemoveField(
            model_name='tarefa',
            name='status',
        ),
        migrations.CreateModel(
            name='ListaTarefas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=55, verbose_name='Nome da Lista')),
                ('numero', models.IntegerField(default=1)),
                ('projeto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projetos.projeto')),
            ],
        ),
        migrations.AddField(
            model_name='tarefa',
            name='lista',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projetos.listatarefas'),
            preserve_default=False,
        ),
    ]