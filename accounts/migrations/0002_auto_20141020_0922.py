# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='householduser',
            old_name='member_household',
            new_name='household',
        ),
        migrations.RenameField(
            model_name='householduser',
            old_name='household_type',
            new_name='user_type',
        ),
        migrations.RemoveField(
            model_name='householduser',
            name='manager_household',
        ),
    ]
