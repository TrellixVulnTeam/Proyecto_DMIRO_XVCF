# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-23 06:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdmiro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IngresosMeses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.CharField(max_length=100)),
                ('valor', models.CharField(max_length=100)),
            ],
        ),
    ]