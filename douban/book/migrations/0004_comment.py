# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-24 03:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20180323_1835'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.IntegerField()),
                ('content', models.CharField(max_length=200)),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Book')),
            ],
        ),
    ]