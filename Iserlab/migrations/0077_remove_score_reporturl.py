# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-16 03:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Iserlab', '0076_remove_score_result_exp_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='reportUrl',
        ),
    ]
