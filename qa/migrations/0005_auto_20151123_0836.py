# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0004_auto_20151123_0547'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='likes_n',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='likes_n',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
