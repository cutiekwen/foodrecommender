# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-01 12:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0004_auto_20171230_0738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersfoodhistory',
            name='date',
            field=models.DateField(default=datetime.date),
        ),
        migrations.AlterField(
            model_name='usersfoodhistory',
            name='userid',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='Username', to='system_user.UserDescription'),
        ),
    ]
