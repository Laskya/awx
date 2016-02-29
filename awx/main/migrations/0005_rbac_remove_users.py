# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rbac_migrations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='admins',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='users',
        ),
        migrations.RemoveField(
            model_name='team',
            name='users',
        ),
    ]
