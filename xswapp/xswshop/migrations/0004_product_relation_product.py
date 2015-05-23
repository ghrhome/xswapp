# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xswshop', '0003_auto_20150522_0057'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='relation_product',
            field=models.ManyToManyField(related_name='relation_product_rel_+', to='xswshop.Product'),
            preserve_default=True,
        ),
    ]
