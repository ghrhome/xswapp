# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appversion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app_version',
            name='app_type',
            field=models.CharField(max_length=20, verbose_name=b'\xe8\xae\xbe\xe5\xa4\x87\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(b'ios', b'ios'), (b'android', b'android')]),
            preserve_default=True,
        ),
    ]
