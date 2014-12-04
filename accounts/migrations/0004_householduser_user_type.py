# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_householduser_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='householduser',
            name='user_type',
            field=models.TextField(null=True, choices=[(b'manager', b'Household Manager'), (b'member', b'Household Member')]),
            preserve_default=True,
        ),
    ]
