# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 14:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20170218_1512'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='status',
        ),
        migrations.AddField(
            model_name='post',
            name='publication_status',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Published')], default='d', max_length=1, verbose_name='Publication Status'),
        ),
    ]