# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xswclass', '0002_auto_20150527_0142'),
    ]

    operations = [
        migrations.CreateModel(
            name='PPTPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img', models.ImageField(upload_to=b'', width_field=480, verbose_name=b'\xe8\xaf\xbe\xe7\xa8\x8b\xe5\x9b\xbe\xe7\x89\x87')),
                ('update_date', models.DateTimeField(verbose_name=b'\xe5\xb9\xbf\xe5\x91\x8a\xe4\xb8\x8a\xe7\xba\xbf\xe6\x97\xb6\xe9\x97\xb4')),
                ('sort_id', models.IntegerField(verbose_name=b'\xe9\xa1\xb5\xe9\x9d\xa2\xe6\x8e\x92\xe5\xba\x8f')),
            ],
            options={
                'verbose_name': '\u6dfb\u52a0\u8bfe\u7a0b\u56fe\u7247',
            },
            bases=(models.Model,),
        ),
        migrations.RenameModel(
            old_name='ClassName',
            new_name='PPTName',
        ),
        migrations.RemoveField(
            model_name='classpage',
            name='classname',
        ),
        migrations.DeleteModel(
            name='ClassPage',
        ),
        migrations.AddField(
            model_name='pptpage',
            name='pptname',
            field=models.ForeignKey(to='xswclass.PPTName'),
            preserve_default=True,
        ),
    ]
