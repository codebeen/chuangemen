# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-01-04 03:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0003_remove_videotype_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='anthology',
            options={'ordering': ('episode', 'video')},
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ('-last_sync_time', 'name')},
        ),
    ]
