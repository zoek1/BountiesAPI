# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-02 00:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bountiestimeline',
            name='avg_fulfillment_amount',
            field=models.DecimalField(decimal_places=2, max_digits=64),
        ),
        migrations.AlterField(
            model_name='bountiestimeline',
            name='total_fulfillment_amount',
            field=models.DecimalField(decimal_places=0, max_digits=64),
        ),
    ]
