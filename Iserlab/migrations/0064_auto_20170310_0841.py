# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-10 08:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Iserlab', '0063_vmimage_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vmimage',
            name='size',
            field=models.BigIntegerField(null=True),
        ),
    ]
