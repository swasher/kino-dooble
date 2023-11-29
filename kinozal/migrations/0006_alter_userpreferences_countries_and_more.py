# Generated by Django 4.2.7 on 2023-11-29 13:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kinozal', '0005_userpreferences_countries_userpreferences_genres_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpreferences',
            name='countries',
            field=models.CharField(blank=True, default=None, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='genres',
            field=models.CharField(blank=True, default=None, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='last_scan',
            field=models.DateField(default=datetime.datetime(2023, 6, 2, 15, 52, 10, 961929)),
        ),
    ]
