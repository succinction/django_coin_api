# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 04:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coin_app', '0008_auto_20170720_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='score',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
            preserve_default=False,
        ),
    ]
