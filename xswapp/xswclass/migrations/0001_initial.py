# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'\xe8\xaf\xbe\xe7\xa8\x8b\xe5\x90\x8d\xe7\xa7\xb0')),
                ('url', models.URLField(max_length=100, verbose_name=b'PPT\xe9\x93\xbe\xe6\x8e\xa5', blank=True)),
                ('date', models.DateTimeField(verbose_name=b'\xe4\xb8\x8a\xe7\xba\xbf\xe6\x97\xa5\xe6\x9c\x9f')),
            ],
            options={
                'verbose_name': '\u521b\u5efa\u8bfe\u7a0b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ClassPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img', models.ImageField(upload_to=b'', width_field=480, verbose_name=b'\xe8\xaf\xbe\xe7\xa8\x8b\xe5\x9b\xbe\xe7\x89\x87')),
                ('update_date', models.DateTimeField(verbose_name=b'\xe5\xb9\xbf\xe5\x91\x8a\xe4\xb8\x8a\xe7\xba\xbf\xe6\x97\xb6\xe9\x97\xb4')),
                ('classname', models.ForeignKey(to='xswclass.ClassName')),
            ],
            options={
                'verbose_name': '\u6dfb\u52a0\u8bfe\u7a0b\u56fe\u7247',
            },
            bases=(models.Model,),
        ),
    ]
