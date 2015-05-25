# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0009_auto_20150525_0146'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answered',
            field=models.BooleanField(default=False, verbose_name=b'\xe5\xb7\xb2\xe8\xa7\xa3\xe5\x86\xb3'),
            preserve_default=True,
        ),
    ]
