# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-04 22:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=20)),
                ('introduction', models.TextField(max_length=500)),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('lastEditTime', models.DateTimeField(auto_now=True)),
                ('author', models.CharField(default='无', max_length=30)),
                ('label', models.IntegerField(null=True)),
                ('cover', models.ImageField(upload_to='book_img')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('labelName', models.CharField(max_length=10)),
                ('labelNum', models.IntegerField()),
            ],
        ),
    ]