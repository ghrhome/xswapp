# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gift', '0007_giftreg_received'),
    ]

    operations = [
        migrations.AddField(
            model_name='gift',
            name='version',
            field=models.CharField(default='0.0.1', max_length=20, verbose_name=b'\xe4\xbf\x83\xe9\x94\x80\xe4\xb8\x8a\xe7\xba\xbf\xe7\x89\x88\xe6\x9c\xac'),
            preserve_default=False,
        ),
    ]
