# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0001_initial'),
        ('qa', '0002_auto_20151117_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='tags',
            field=models.ManyToManyField(to='lib.Tag'),
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(to='lib.Tag'),
        ),
    ]
