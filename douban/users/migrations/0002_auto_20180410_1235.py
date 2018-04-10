# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-10 12:35
from __future__ import unicode_literals

from django.db import migrations, models
import main.storage


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='head_img',
            field=models.ImageField(default='', storage=main.storage.ImageStorage(), upload_to='head_img'),
        ),
        migrations.AddField(
            model_name='user',
            name='motto',
            field=models.CharField(default='', max_length=25),
        ),
    ]