# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-23 08:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintain', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nodehierarchy',
            name='node_type',
            field=models.IntegerField(choices=[(1, '子节点'), (2, '叶子节点'), (0, '根节点')], default=0),
        ),
    ]