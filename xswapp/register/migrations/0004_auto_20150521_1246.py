# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_auto_20150521_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userparent',
            name='loc_area',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'parent_id', to='register.Area', chained_field=b'loc_area'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userparent',
            name='loc_city',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'parent_id', to='register.City', chained_field=b'loc_provinc'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userteacher',
            name='loc_area',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'parent_id', to='register.Area', chained_field=b'loc_city'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userteacher',
            name='loc_city',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'parent_id', to='register.City', chained_field=b'loc_province'),
            preserve_default=True,
        ),
    ]
