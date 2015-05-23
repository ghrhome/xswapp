# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xswshop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='shop_url',
        ),
        migrations.AddField(
            model_name='product',
            name='shop_url_tmall',
            field=models.URLField(default=b'http://lion.tmall.com/category-367325168.htm?spm=a1z10.1-b.w9154402-9436601579.6.QIgjSC', verbose_name=b'\xe5\xa4\xa9\xe7\x8c\xab\xe8\xb4\xad\xe4\xb9\xb0\xe9\x93\xbe\xe6\x8e\xa5', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='shop_url_yhd',
            field=models.URLField(verbose_name=b'\xe4\xba\xac\xe4\xb8\x9c\xe8\xb4\xad\xe4\xb9\xb0\xe9\x93\xbe\xe6\x8e\xa5', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='title_img',
            field=models.ImageField(default='/media/title.png', upload_to=b'', verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe5\x90\x8d\xe7\xa7\xb0\xe5\x9b\xbe\xe7\x89\x87'),
            preserve_default=False,
        ),
    ]
