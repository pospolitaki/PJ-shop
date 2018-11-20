# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-18 19:36
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0007_auto_20181109_1345'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'order', 'verbose_name_plural': 'orders'},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name': 'order item', 'verbose_name_plural': 'order items'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'Status', 'verbose_name_plural': 'Statuses'},
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_email',
            field=models.EmailField(blank=True, default=None, max_length=254, null=True, verbose_name='customer email'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_phone_number',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number should be entered in the format: '+38099.......'.", regex='^\\+?1?\\d{9,15}$')], verbose_name='customer phone number'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_ordered',
            field=models.DateTimeField(auto_now=True, verbose_name='date ordered'),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_ordered',
            field=models.BooleanField(default=False, verbose_name='is ordered'),
        ),
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='shopping_cart.OrderItem', verbose_name='items'),
        ),
        migrations.AlterField(
            model_name='order',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='accounts.Profile', verbose_name='owner'),
        ),
        migrations.AlterField(
            model_name='order',
            name='ref_code',
            field=models.CharField(max_length=15, verbose_name='order code'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shopping_cart.Status', verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date added'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='date_ordered',
            field=models.DateTimeField(null=True, verbose_name='date ordered'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='details',
            field=models.CharField(blank=True, max_length=140, verbose_name='details'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='is_ordered',
            field=models.BooleanField(default=False, verbose_name='is ordered'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='nmb',
            field=models.IntegerField(default=1, verbose_name='quantity'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='price_per_item',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='price per item'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Product', verbose_name='product'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='total price'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='updated'),
        ),
        migrations.AlterField(
            model_name='status',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='status',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is active'),
        ),
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=24, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='status',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='updated'),
        ),
    ]