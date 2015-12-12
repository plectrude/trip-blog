# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titolo', models.CharField(max_length=200)),
                ('testo', models.TextField()),
                ('data_creazione', models.DateTimeField(default=django.utils.timezone.now)),
                ('data_pubblicazione', models.DateTimeField(null=True, blank=True)),
                ('autore', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
