# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20141020_0922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='householduser',
            name='user_type',
        ),
    ]
