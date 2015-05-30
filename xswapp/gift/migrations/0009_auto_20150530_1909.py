# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gift', '0008_gift_version'),
    ]

    operations = [
        migrations.AddField(
            model_name='giftreg',
            name='user_phone',
            field=models.CharField(default='1300000000', max_length=b'20', verbose_name=b'\xe6\x89\x8b\xe6\x9c\xba\xe5\x8f\xb7\xe7\xa0\x81'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='giftreg',
            name='username',
            field=models.CharField(default='', max_length=b'20', verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\xa7\x93\xe5\x90\x8d'),
            preserve_default=False,
        ),
    ]
