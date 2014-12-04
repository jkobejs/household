# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import accounts.models
import common.utils


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_householduser_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='householduser',
            name='photo',
            field=models.ImageField(default=None, storage=accounts.models.OverwriteStorage(), upload_to=common.utils.upload_to_callable),
        ),
    ]
