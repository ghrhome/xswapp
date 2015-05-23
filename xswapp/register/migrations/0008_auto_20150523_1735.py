# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0007_auto_20150521_1301'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userparent',
            options={'verbose_name': '\u5bb6\u957f'},
        ),
        migrations.AlterModelOptions(
            name='userteacher',
            options={'verbose_name': '\u8001\u5e08'},
        ),
    ]
