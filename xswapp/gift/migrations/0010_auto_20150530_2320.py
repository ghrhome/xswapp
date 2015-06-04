# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gift', '0009_auto_20150530_1909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='giftreg',
            name='user_phone',
        ),
        migrations.RemoveField(
            model_name='giftreg',
            name='username',
        ),
    ]
