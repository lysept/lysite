# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-20 07:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Iserlab', '0093_score_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='score',
            old_name='status',
            new_name='instance_status',
        ),
    ]
