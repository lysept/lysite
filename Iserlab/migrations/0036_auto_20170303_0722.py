# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-03 07:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Iserlab', '0035_auto_20170302_0810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='exp_guide',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='exp_reportDIR',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='exp_result',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]