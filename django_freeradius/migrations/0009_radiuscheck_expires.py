# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_freeradius', '0008_auto_20171004_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='radiuscheck',
            name='expires',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
