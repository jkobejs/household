# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('household', '0002_auto_20141106_1744'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=255)),
                ('amount', models.IntegerField()),
                ('transaction_type', models.BooleanField(default=True, choices=[(True, b'Add money'), (False, b'Withdraw money')])),
                ('household', models.ForeignKey(default=None, to='household.Household')),
                ('household_user', models.ForeignKey(default=None, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date_created'],
            },
            bases=(models.Model,),
        ),
    ]
