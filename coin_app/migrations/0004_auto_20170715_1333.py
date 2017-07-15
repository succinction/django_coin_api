# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 20:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coin_app', '0003_auto_20170714_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='cheat',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='game',
            name='duration',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]