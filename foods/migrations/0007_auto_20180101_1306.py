# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-01 13:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0006_auto_20180101_1300'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usersfoodhistory',
            old_name='userid',
            new_name='user',
        ),
    ]