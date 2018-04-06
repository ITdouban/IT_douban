# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-05 06:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_auto_20180405_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='owner',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='编辑人'),
        ),
    ]