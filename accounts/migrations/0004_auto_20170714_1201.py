# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-14 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20170713_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='guest_number',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
