# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-11 03:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20170209_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='repo',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
