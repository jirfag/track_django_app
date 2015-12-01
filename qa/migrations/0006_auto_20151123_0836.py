# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0005_auto_20151123_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='likes_n',
            field=models.IntegerField(null=True),
        ),
    ]
