# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20141113_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='householduser',
            name='photo',
            field=models.ImageField(default=None, upload_to=b'profiles'),
            preserve_default=True,
        ),
    ]
