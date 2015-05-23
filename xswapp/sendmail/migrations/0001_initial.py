# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maillist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name=b'\xe9\x82\xae\xe4\xbb\xb6\xe6\xa0\x87\xe9\xa2\x98')),
                ('body', models.TextField(verbose_name=b'\xe9\x82\xae\xe4\xbb\xb6\xe5\x86\x85\xe5\xae\xb9')),
                ('mail_src', models.URLField(max_length=100, verbose_name=b'\xe9\x82\xae\xe4\xbb\xb6\xe8\xb5\x84\xe6\xba\x90\xe5\x9c\xb0\xe5\x9d\x80')),
            ],
            options={
                'verbose_name': '\u90ae\u4ef6\u4e0b\u8f7d',
                'verbose_name_plural': '\u90ae\u4ef6\u4e0b\u8f7d',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PPT',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name=b'PPT\xe6\xa0\x87\xe9\xa2\x98')),
                ('ppt', models.FileField(upload_to=b'', verbose_name=b'PPT')),
            ],
            options={
                'verbose_name': 'PPT',
                'verbose_name_plural': 'PPT',
            },
            bases=(models.Model,),
        ),
    ]
