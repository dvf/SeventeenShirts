# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_order',
        ),
        migrations.AddField(
            model_name='order',
            name='product_order',
            field=models.ManyToManyField(to='shop.Order', through='shop.ProductOrder'),
        ),
    ]
