# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-28 00:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdmiro', '0010_agencias_asesores_productos_trasacciones'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trasacciones',
            name='tra_valor',
            field=models.PositiveIntegerField(max_length=10),
        ),
    ]