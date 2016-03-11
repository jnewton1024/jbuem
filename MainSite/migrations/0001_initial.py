# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-10 00:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField()),
                ('btc_power', models.CharField(max_length=50)),
                ('power_factor', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pyranometer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField()),
                ('kandz', models.CharField(max_length=50)),
                ('eppely', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Solar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField()),
                ('enphase_power', models.CharField(max_length=50)),
                ('fronius_power', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Wind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField()),
                ('wind_speed', models.CharField(max_length=50)),
                ('wind_direction', models.CharField(max_length=50)),
                ('humidity', models.CharField(max_length=50)),
                ('temperature', models.CharField(max_length=50)),
                ('wind_power', models.CharField(max_length=50)),
            ],
        ),
    ]
