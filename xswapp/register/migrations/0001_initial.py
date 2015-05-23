# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AsAreas',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('area_name', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'as_areas',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.CharField(max_length=300, verbose_name=b'\xe5\x9b\x9e\xe5\xa4\x8d')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x9b\x9e\xe5\xa4\x8d\xe6\x97\xa5\xe6\x9c\x9f')),
            ],
            options={
                'verbose_name': '\u610f\u89c1\u56de\u590d',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('area', models.CharField(max_length=50, verbose_name=b'\xe5\x8c\xba')),
                ('zipcode', models.CharField(max_length=6)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('city', models.CharField(max_length=50, verbose_name=b'\xe5\xb8\x82')),
                ('zipcode', models.CharField(max_length=6)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('province', models.CharField(max_length=50, verbose_name=b'\xe7\x9c\x81')),
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
                ('question', models.CharField(max_length=500, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe6\x84\x8f\xe8\xa7\x81')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u610f\u89c1',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=50, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d')),
                ('phone', models.CharField(max_length=11, verbose_name=b'\xe6\x89\x8b\xe6\x9c\xba\xe5\x8f\xb7\xe7\xa0\x81')),
                ('password', models.CharField(max_length=50, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81')),
                ('user_type', models.CharField(default=b'parent', max_length=30, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(b'parent', b'\xe5\xae\xb6\xe9\x95\xbf'), (b'teacher', b'\xe6\x95\x99\xe5\xb8\x88')])),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '\u7528\u6237',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserParent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('real_name', models.CharField(max_length=50, verbose_name=b'\xe7\x9c\x9f\xe5\xae\x9e\xe5\xa7\x93\xe5\x90\x8d')),
                ('baby_name', models.CharField(max_length=50, verbose_name=b'\xe5\xae\x9d\xe8\xb4\x9d\xe5\xa7\x93\xe5\x90\x8d')),
                ('baby_birth', models.DateField(verbose_name=b'\xe5\x87\xba\xe7\x94\x9f\xe6\x97\xa5\xe6\x9c\x9f')),
                ('baby_sex', models.CharField(default=b'boy', max_length=12, verbose_name=b'\xe5\xae\x9d\xe8\xb4\x9d\xe6\x80\xa7\xe5\x88\xab', choices=[(b'boy', b'\xe7\x94\xb7\xe5\xad\xa9'), (b'girl', b'\xe5\xa5\xb3\xe5\xad\xa9')])),
                ('loc_detail', models.CharField(max_length=100, verbose_name=b'\xe8\xaf\xa6\xe7\xbb\x86\xe5\x9c\xb0\xe5\x9d\x80', blank=True)),
                ('grade', models.CharField(max_length=10, verbose_name=b'\xe5\xae\x9d\xe8\xb4\x9d\xe5\xad\xa6\xe9\xbe\x84', blank=True)),
                ('school', models.CharField(max_length=100, verbose_name=b'\xe5\xad\xa6\xe6\xa0\xa1\xe5\x90\x8d\xe7\xa7\xb0', blank=True)),
                ('relation', models.CharField(max_length=20, verbose_name=b'\xe5\xae\x9d\xe8\xb4\x9d\xe5\x85\xb3\xe7\xb3\xbb', choices=[(b'mom', b'\xe5\xa6\x88\xe5\xa6\x88'), (b'dad', b'\xe7\x88\xb8\xe7\x88\xb8'), (b'grandma', b'\xe5\xa5\xb6\xe5\xa5\xb6'), (b'grandpa', b'\xe7\x88\xb7\xe7\x88\xb7'), (b'mat_grandma', b'\xe5\xa4\x96\xe5\xa9\x86'), (b'mat_grandpa', b'\xe5\xa4\x96\xe5\x85\xac')])),
                ('loc_area', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'city', to='register.Area', chained_field=b'loc_city')),
                ('loc_city', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'province', to='register.City', chained_field=b'loc_province')),
                ('loc_province', models.ForeignKey(to='register.Province')),
                ('user', models.ForeignKey(to='register.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserTeacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gender', models.CharField(max_length=10, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[(b'mr', b'\xe5\x85\x88\xe7\x94\x9f'), (b'mrs', b'\xe5\xb0\x8f\xe5\xa7\x90')])),
                ('real_name', models.CharField(max_length=50, verbose_name=b'\xe7\x9c\x9f\xe5\xae\x9e\xe5\xa7\x93\xe5\x90\x8d')),
                ('loc_detail', models.CharField(max_length=100, verbose_name=b'\xe8\xaf\xa6\xe7\xbb\x86\xe5\x9c\xb0\xe5\x9d\x80', blank=True)),
                ('grade', models.CharField(max_length=10, verbose_name=b'\xe4\xbb\xbb\xe6\x95\x99\xe5\xb9\xb4\xe7\xba\xa7', blank=True)),
                ('school', models.CharField(max_length=100, verbose_name=b'\xe5\xad\xa6\xe6\xa0\xa1\xe5\x90\x8d\xe7\xa7\xb0 ', blank=True)),
                ('loc_area', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'city', to='register.Area', chained_field=b'loc_city')),
                ('loc_city', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'province', to='register.City', chained_field=b'loc_province')),
                ('loc_province', models.ForeignKey(to='register.Province')),
                ('user', models.ForeignKey(to='register.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='question',
            name='user',
            field=models.ForeignKey(to='register.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='city',
            name='parent_id',
            field=models.ForeignKey(to='register.Province'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='area',
            name='parent_id',
            field=models.ForeignKey(to='register.City'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='register.Question'),
            preserve_default=True,
        ),
    ]
