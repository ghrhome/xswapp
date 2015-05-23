# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gift', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giftitem',
            name='img',
            field=models.ImageField(upload_to=b'', verbose_name=b'\xe5\xb9\xbf\xe5\x91\x8a\xe9\xa1\xb5'),
            preserve_default=True,
        ),
    ]
