# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='answers',
        ),
        migrations.AddField(
            model_name='answer',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 17, 21, 47, 17, 80488, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='answers',
            field=models.ManyToManyField(to='qa.Answer'),
        ),
    ]
