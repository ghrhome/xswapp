# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userparent',
            name='loc_area',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'city', to='register.Area', chained_field=b'parent_id'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userparent',
            name='loc_city',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'province', to='register.City', chained_field=b'parent_id'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userteacher',
            name='loc_area',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'city', to='register.Area', chained_field=b'parent_id'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userteacher',
            name='loc_city',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'province', to='register.City', chained_field=b'parent_id'),
            preserve_default=True,
        ),
    ]
