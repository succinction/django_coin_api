# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 04:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20170720_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='best_score',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='user',
            name='overall_score',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='user',
            name='score',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
