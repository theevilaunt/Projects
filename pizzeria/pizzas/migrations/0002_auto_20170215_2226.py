# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-02-15 22:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Toppings',
            new_name='Pizza_Toppings',
        ),
    ]
