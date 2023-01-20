# Generated by Django 3.2.16 on 2023-01-20 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0001_initial'),
        ('booking', '0003_auto_20230120_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='useraccount.userprofile'),
        ),
    ]
