# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gift', '0003_giftitem_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='giftitem',
            name='reg_user',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
