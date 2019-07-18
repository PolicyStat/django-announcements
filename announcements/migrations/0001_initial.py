# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-18 12:06
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('content', models.TextField(verbose_name='content')),
                ('creation_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='creation_date')),
                ('site_wide', models.BooleanField(db_index=True, default=False, verbose_name='site wide')),
                ('members_only', models.BooleanField(default=False, verbose_name='members only')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='creator')),
            ],
            options={
                'verbose_name': 'announcement',
                'verbose_name_plural': 'announcements',
            },
        ),
    ]
