# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-03-16 20:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techGyaan', '0003_auto_20170316_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
