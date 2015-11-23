# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0003_auto_20151123_0538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='question',
            name='answers',
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(default=0, to='qa.Question'),
            preserve_default=False,
        ),
    ]
