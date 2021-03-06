# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-16 05:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('foods', '0008_foods_image'),
        ('system_user', '0025_auto_20180116_0525'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('archived', models.BooleanField(default=False)),
                ('and_user_diet_is', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system_user.Diet')),
                ('if_food_diet_is', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foods.Diet')),
            ],
            options={
                'verbose_name': 'Rule',
                'verbose_name_plural': 'Rules',
            },
        ),
        migrations.CreateModel(
            name='WorkingMemory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('archived', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Working Memory',
                'verbose_name_plural': 'Working Memory',
            },
        ),
    ]
