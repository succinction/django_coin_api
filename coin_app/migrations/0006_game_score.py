# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 07:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coin_app', '0005_auto_20170715_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='score',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
