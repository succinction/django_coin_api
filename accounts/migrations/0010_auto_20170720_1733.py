# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 00:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_user_overall_score'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-overall_score']},
        ),
    ]