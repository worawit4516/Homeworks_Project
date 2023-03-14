# Generated by Django 4.1.7 on 2023-03-06 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homeworks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stu_homework',
            fields=[
                ('homework_id', models.AutoField(primary_key=True, serialize=False)),
                ('homework_name', models.CharField(blank=True, max_length=20, null=True)),
                ('homework_description', models.CharField(blank=True, max_length=250, null=True)),
                ('homework_room', models.CharField(blank=True, max_length=12, null=True)),
                ('homework_data', models.CharField(blank=True, max_length=1200, null=True)),
            ],
        ),
    ]
