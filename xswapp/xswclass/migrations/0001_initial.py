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
                ('url', models.URLField(max_length=100, verbose_name=b'PPT\xe9\x93\xbe\xe6\x8e\xa5')),
                ('date', models.DateTimeField(auto_now=True)),
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
                ('classname', models.ForeignKey(to='xswclass.ClassName')),
            ],
            options={
                'verbose_name': '\u6dfb\u52a0\u8bfe\u7a0b\u56fe\u7247',
            },
            bases=(models.Model,),
        ),
    ]
