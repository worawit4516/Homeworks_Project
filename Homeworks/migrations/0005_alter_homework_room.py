# Generated by Django 4.1.7 on 2023-03-06 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Homeworks', '0004_remove_homework_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Homeworks.room'),
        ),
    ]
