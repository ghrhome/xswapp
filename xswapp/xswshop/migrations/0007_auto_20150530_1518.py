# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xswshop', '0006_auto_20150527_0142'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='bottom_left_link',
            field=models.URLField(default=b'', verbose_name=b'\xe5\xba\x95\xe9\x83\xa8\xe5\xb7\xa6\xe4\xbe\xa7\xe9\x93\xbe\xe6\x8e\xa5'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='bottom_left_product',
            field=models.ImageField(default=b'', upload_to=b'', verbose_name=b'\xe5\xba\x95\xe9\x83\xa8\xe5\xb7\xa6\xe4\xbe\xa7\xe5\x9b\xbe\xe7\x89\x87'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='bottom_right_link',
            field=models.URLField(default=b'http://lion.tmall.com/category-367325168.htm?spm=a1z10.1-b.w9154402-9436601579.6.QIgjSC', verbose_name=b'\xe5\xba\x95\xe9\x83\xa8\xe5\x8f\xb3\xe4\xbe\xa7\xe9\x93\xbe\xe6\x8e\xa5'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='bottom_right_product',
            field=models.ImageField(default=b'', upload_to=b'', verbose_name=b'\xe5\xba\x95\xe9\x83\xa8\xe5\x8f\xb3\xe4\xbe\xa7\xe5\x9b\xbe\xe7\x89\x87'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='share_info',
            field=models.CharField(default=b'\xe5\xb0\x8f\xe7\x8b\xae\xe7\x8e\x8b\xe6\x98\xaf\xe7\x94\xb1\xe5\x88\x9b\xe5\xa7\x8b\xe4\xba\x8e1891\xe5\xb9\xb4\xe7\x9a\x84\xe6\x97\xa5\xe6\x9c\xac\xe7\x8b\xae\xe7\x8e\x8b\xe5\x87\xba\xe5\x93\x81\xe7\x9a\x84\xef\xbc\x8c\xe4\xbb\xa5\xe8\xb6\x85\xe8\xbf\x87120\xe5\xb9\xb4\xe7\x9a\x84\xe4\xbc\xa0\xe6\x89\xbf\xe7\xbb\x8f\xe9\xaa\x8c\xe5\x92\x8c\xe9\xa2\x86\xe5\x85\x88\xe7\xa7\x91\xe6\x8a\x80\xef\xbc\x8c\xe8\xaf\x9a\xe6\x8c\x9a\xe4\xb8\xba\xe6\x82\xa8\xe7\x9a\x84\xe5\xad\xa9\xe5\xad\x90\xe6\x8f\x90\xe4\xbe\x9b\xe5\xae\x89\xe5\x85\xa8\xe4\xbc\x98\xe8\xb4\xa8\xe7\x9a\x84\xe5\x8f\xa3\xe8\x85\x94\xe6\x8a\xa4\xe7\x90\x86\xe4\xba\xa7\xe5\x93\x81\xe3\x80\x82', max_length=200, verbose_name=b'\xe5\x88\x86\xe4\xba\xab\xe4\xbf\xa1\xe6\x81\xaf', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='version',
            field=models.CharField(default=b'0.0.1', max_length=20, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe7\x89\x88\xe6\x9c\xac'),
            preserve_default=True,
        ),
    ]
