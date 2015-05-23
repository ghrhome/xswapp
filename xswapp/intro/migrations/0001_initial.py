# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Intro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name=b'\xe5\xb0\x8f\xe7\x8b\xae\xe7\x8e\x8b\xe7\xae\x80\xe4\xbb\x8b')),
                ('intro', models.TextField(verbose_name=b'\xe7\xae\x80\xe4\xbb\x8b')),
            ],
            options={
                'verbose_name': '\u5c0f\u72ee\u738b\u7b80\u4ecb',
            },
            bases=(models.Model,),
        ),
    ]
