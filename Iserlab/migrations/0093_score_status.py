# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-20 06:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Iserlab', '0092_vminstance'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='status',
            field=models.CharField(blank=True, default='UNLAUNCHED', max_length=20, null=True),
        ),
    ]
