# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Download',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('download_title', models.CharField(max_length=100, verbose_name=b'\xe4\xb8\x8b\xe8\xbd\xbd\xe6\xa0\x87\xe9\xa2\x98')),
                ('download_intro', ckeditor.fields.RichTextField()),
                ('download_src', models.FileField(upload_to=b'', max_length=200, verbose_name=b'\xe4\xb8\x8b\xe8\xbd\xbd\xe8\xb5\x84\xe6\xba\x90')),
                ('download_num', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': '\u4e0b\u8f7d',
                'verbose_name_plural': '\u4e0b\u8f7d',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Hometown',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('parent_id', models.IntegerField()),
                ('area_name', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=6)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(to='xswtest.Question'),
            preserve_default=True,
        ),
    ]
