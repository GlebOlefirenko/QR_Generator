# Generated by Django 5.1.4 on 2025-02-15 18:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0005_alter_account_sub_expire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='sub_expire',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 15, 19, 34, 45, 810504)),
        ),
    ]
