# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xswshop', '0004_product_relation_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='background_color',
            field=models.CharField(default=b'#c5e1eb', max_length=20, verbose_name=b'\xe8\x83\x8c\xe6\x99\xaf\xe9\xa2\x9c\xe8\x89\xb2'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='sort_id',
            field=models.IntegerField(default=1, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe6\x8e\x92\xe5\xba\x8f', blank=True),
            preserve_default=True,
        ),
    ]
