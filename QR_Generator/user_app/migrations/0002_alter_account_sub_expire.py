# Generated by Django 5.1.5 on 2025-02-01 20:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='sub_expire',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 1, 21, 12, 20, 910674)),
        ),
    ]
