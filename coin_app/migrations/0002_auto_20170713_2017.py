# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-14 03:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coin_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='gameNumber',
            field=models.PositiveIntegerField(),
        ),
    ]
