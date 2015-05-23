# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'\xe7\xa6\x8f\xe5\x88\xa9\xe5\x90\x8d\xe7\xa7\xb0')),
                ('date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u798f\u5229',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GiftItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img', models.ImageField(upload_to=b'', width_field=480, verbose_name=b'\xe5\xb9\xbf\xe5\x91\x8a\xe9\xa1\xb5')),
                ('img_url', models.URLField(max_length=100, verbose_name=b'\xe4\xbf\x83\xe9\x94\x80\xe9\x93\xbe\xe6\x8e\xa5')),
                ('gift', models.ForeignKey(to='gift.Gift')),
            ],
            options={
                'verbose_name': '\u4fc3\u9500\u5e7f\u544a',
            },
            bases=(models.Model,),
        ),
    ]
