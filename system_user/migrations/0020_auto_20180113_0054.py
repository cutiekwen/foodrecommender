# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-13 00:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_user', '0019_auto_20180112_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdescription',
            name='birthday',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 13, 0, 54, 2, 617982)),
        ),
    ]
