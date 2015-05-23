# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xswshop', '0002_auto_20150522_0052'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='shop_url_jd',
            field=models.URLField(verbose_name=b'\xe4\xba\xac\xe4\xb8\x9c\xe8\xb4\xad\xe4\xb9\xb0\xe9\x93\xbe\xe6\x8e\xa5', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='shop_url_yhd',
            field=models.URLField(verbose_name=b'\xe4\xb8\x80\xe5\x8f\xb7\xe5\xba\x97\xe8\xb4\xad\xe4\xb9\xb0\xe9\x93\xbe\xe6\x8e\xa5', blank=True),
            preserve_default=True,
        ),
    ]
