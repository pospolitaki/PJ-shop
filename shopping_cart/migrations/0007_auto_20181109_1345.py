# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-09 13:45
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0006_auto_20181108_1213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='profile',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='details',
            field=models.CharField(blank=True, max_length=140),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_phone_number',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number should be entered in the format: '+38099.......'.", regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shopping_cart.Status'),
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]
