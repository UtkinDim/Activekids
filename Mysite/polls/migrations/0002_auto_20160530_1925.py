# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 16:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choice_test',
            new_name='choice_text',
        ),
    ]
