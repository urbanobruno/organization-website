# Generated by Django 3.2.5 on 2021-09-25 18:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]