# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xswshop', '0005_auto_20150526_0427'),
    ]

    operations = [
        migrations.AddField(
            model_name='catelog',
            name='version',
            field=models.CharField(default='0.0.1', max_length=20, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe7\xb1\xbb\xe5\x9e\x8b\xe7\x89\x88\xe6\x9c\xac'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='version',
            field=models.CharField(default='0.0.1', max_length=20, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe7\x89\x88\xe6\x9c\xac'),
            preserve_default=False,
        ),
    ]
