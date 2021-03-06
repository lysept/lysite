# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-19 03:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Iserlab', '0084_auto_20170319_0304'),
    ]

    operations = [
        migrations.CreateModel(
            name='TempExp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exp_name', models.CharField(max_length=150)),
                ('exp_description', models.TextField(blank=True, max_length=500)),
                ('exp_createtime', models.DateTimeField(auto_now_add=True)),
                ('exp_updatetime', models.DateTimeField(auto_now=True)),
                ('exp_image_count', models.IntegerField(blank=True, null=True)),
                ('exp_guide', models.TextField(blank=True, null=True)),
                ('exp_guide_path', models.CharField(blank=True, max_length=300, null=True)),
                ('exp_result', models.CharField(blank=True, max_length=500, null=True)),
                ('exp_reportDIR', models.CharField(blank=True, max_length=150, null=True)),
                ('is_shared', models.BooleanField(default=False)),
                ('shared_time', models.DateTimeField(blank=True, null=True)),
                ('VM_count', models.IntegerField(default=0, null=True)),
                ('exp_images', models.ManyToManyField(to='Iserlab.VMImage')),
                ('exp_network', models.ManyToManyField(to='Iserlab.Network')),
                ('exp_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Iserlab.User')),
            ],
            options={
                'ordering': ['-exp_createtime'],
            },
        ),
        migrations.CreateModel(
            name='TempGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.TextField(blank=True, max_length=100, null=True)),
                ('stuCount', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('student', models.ManyToManyField(to='Iserlab.Student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Iserlab.User')),
            ],
        ),
    ]
