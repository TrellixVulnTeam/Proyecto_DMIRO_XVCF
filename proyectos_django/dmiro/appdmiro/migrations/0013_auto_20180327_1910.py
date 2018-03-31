# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-28 00:10
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdmiro', '0012_auto_20180327_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trasacciones',
            name='tra_valor',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(3)]),
        ),
    ]