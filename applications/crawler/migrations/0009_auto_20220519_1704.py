# Generated by Django 3.1.7 on 2022-05-19 17:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0008_auto_20220519_1619'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['creation', 'pub_date'], 'verbose_name_plural': 'News'},
        ),
        migrations.AddField(
            model_name='news',
            name='creation',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 19, 17, 4, 59, 104463)),
        ),
    ]
