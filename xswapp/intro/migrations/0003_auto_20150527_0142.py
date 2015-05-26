# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('intro', '0002_intro_intro_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='intro',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 26, 17, 42, 7, 402654, tzinfo=utc), verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xa5\xe6\x9c\x9f', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='intro',
            name='version',
            field=models.CharField(default='0.0.1', max_length=20, verbose_name=b'\xe7\xae\x80\xe4\xbb\x8b\xe7\x89\x88\xe6\x9c\xac\xe5\x8f\xb7'),
            preserve_default=False,
        ),
    ]
