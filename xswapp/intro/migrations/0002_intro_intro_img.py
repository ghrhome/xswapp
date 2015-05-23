# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='intro',
            name='intro_img',
            field=models.ImageField(default='', upload_to=b'', verbose_name=b'\xe7\xae\x80\xe4\xbb\x8b\xe9\x85\x8d\xe5\x9b\xbe'),
            preserve_default=False,
        ),
    ]
