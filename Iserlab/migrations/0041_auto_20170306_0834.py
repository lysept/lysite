# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-06 08:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Iserlab', '0040_auto_20170306_0710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='exp',
        ),
        migrations.RemoveField(
            model_name='score',
            name='stu',
        ),
        migrations.DeleteModel(
            name='Score',
        ),
    ]