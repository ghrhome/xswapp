# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xswclass', '0003_auto_20150527_0215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pptpage',
            name='img',
            field=models.ImageField(upload_to=b'', verbose_name=b'\xe8\xaf\xbe\xe7\xa8\x8b\xe5\x9b\xbe\xe7\x89\x87'),
            preserve_default=True,
        ),
    ]
