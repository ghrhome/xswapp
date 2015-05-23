# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gift', '0002_auto_20150521_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='giftitem',
            name='title',
            field=models.CharField(default='\u6682\u65e0', max_length=50, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98'),
            preserve_default=False,
        ),
    ]
