# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xswshop', '0007_auto_20150530_1518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='relation_product',
        ),
    ]
