# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-10 02:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0004_auto_20171205_2117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagelocation',
            name='series',
        ),
    ]
