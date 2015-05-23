# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App_Version',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.CharField(max_length=200, verbose_name=b'\xe7\x89\x88\xe6\x9c\xac\xe5\x8f\xb7')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xa5\xe6\x9c\x9f')),
                ('app_type', models.CharField(max_length=20, verbose_name=b'\xe8\xae\xbe\xe5\xa4\x87\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('app_url', models.URLField(verbose_name=b'\xe4\xb8\x8b\xe8\xbd\xbd\xe9\x93\xbe\xe6\x8e\xa5')),
            ],
            options={
                'verbose_name': 'app\u7248\u672c',
            },
            bases=(models.Model,),
        ),
    ]
