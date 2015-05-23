# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0007_auto_20150521_1301'),
        ('gift', '0004_giftitem_reg_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='GiftReg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('gift', models.ForeignKey(to='gift.GiftItem')),
                ('user', models.ForeignKey(to='register.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='giftitem',
            name='reg_user',
            field=models.BooleanField(default=False, verbose_name=b'\xe6\xb3\xa8\xe5\x86\x8c\xe9\x99\x90\xe5\x88\xb6'),
            preserve_default=True,
        ),
    ]
