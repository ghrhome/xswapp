# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gift', '0006_auto_20150523_0321'),
    ]

    operations = [
        migrations.AddField(
            model_name='giftreg',
            name='received',
            field=models.BooleanField(default=False, verbose_name=b'\xe5\xb7\xb2\xe9\xa2\x86\xe5\x8f\x96'),
            preserve_default=True,
        ),
    ]
