# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_householduser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='householduser',
            name='household',
            field=models.ForeignKey(related_name=b'members', default=None, to='household.Household', null=True),
        ),
    ]
