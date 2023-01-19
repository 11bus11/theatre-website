# Generated by Django 3.2.16 on 2023-01-19 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Play',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('description', models.CharField(default='To be added', max_length=1000)),
            ],
            options={
                'verbose_name_plural': 'Plays',
            },
        ),
    ]
