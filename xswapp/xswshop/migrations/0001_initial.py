# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catelog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe7\xb1\xbb\xe5\x9e\x8b')),
            ],
            options={
                'verbose_name': '\u4ea7\u54c1\u7c7b\u578b',
                'verbose_name_plural': '\u4ea7\u54c1\u7c7b\u578b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_name', models.CharField(max_length=50, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe5\x90\x8d\xe7\xa7\xb0')),
                ('thumb_nail', models.ImageField(upload_to=b'', verbose_name=b'\xe7\xbc\xa9\xe7\x95\xa5\xe5\x9b\xbe')),
                ('shop_url', models.URLField(default=b'http://www.tmall.com', verbose_name=b'\xe8\xb4\xad\xe4\xb9\xb0\xe9\x93\xbe\xe6\x8e\xa5')),
                ('product_img', models.ImageField(upload_to=b'', verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe5\x9b\xbe\xe7\x89\x87')),
                ('product_detail', ckeditor.fields.RichTextField()),
                ('catelog', models.ForeignKey(to='xswshop.Catelog')),
            ],
            options={
                'verbose_name': '\u4ea7\u54c1',
                'verbose_name_plural': '\u4ea7\u54c1',
            },
            bases=(models.Model,),
        ),
    ]
