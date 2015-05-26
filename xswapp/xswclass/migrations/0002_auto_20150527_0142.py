# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xswclass', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classname',
            name='version',
            field=models.CharField(default='0.0.1', max_length=20, verbose_name=b'ppt\xe7\x89\x88\xe6\x9c\xac'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='classpage',
            name='sort_id',
            field=models.IntegerField(default=1, verbose_name=b'\xe9\xa1\xb5\xe9\x9d\xa2\xe6\x8e\x92\xe5\xba\x8f'),
            preserve_default=False,
        ),
    ]
