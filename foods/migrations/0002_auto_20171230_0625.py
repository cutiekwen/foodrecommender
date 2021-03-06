# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-30 06:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diet_type', models.CharField(max_length=200)),
                ('notes', models.TextField(blank=True, default='', null=True)),
                ('archived', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Diet',
                'verbose_name_plural': 'Diets',
            },
        ),
        migrations.CreateModel(
            name='Foods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('notes', models.TextField(blank=True, default='', null=True)),
                ('calories', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name=())),
                ('protein', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name=())),
                ('fat', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name=())),
                ('carbohydrates', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name=())),
                ('archived', models.BooleanField(default=False)),
                ('diet', models.ManyToManyField(to='foods.Diet')),
            ],
            options={
                'verbose_name': 'Food',
                'verbose_name_plural': 'Foods',
            },
        ),
        migrations.AlterModelOptions(
            name='ingredient',
            options={'verbose_name': 'Ingredient', 'verbose_name_plural': 'Ingredients'},
        ),
        migrations.AddField(
            model_name='ingredient',
            name='archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='calories',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name=()),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='carbohydrates',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name=()),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='fat',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name=()),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='protein',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name=()),
        ),
        migrations.AddField(
            model_name='foods',
            name='ingredients',
            field=models.ManyToManyField(to='foods.Ingredient'),
        ),
    ]
