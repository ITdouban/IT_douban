# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-13 18:03
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
                ('bookname', models.CharField(max_length=30, verbose_name='书名')),
                ('originName', models.CharField(default='', max_length=30, verbose_name='原作名')),
                ('introduction', models.TextField(max_length=500, verbose_name='简介')),
                ('createTime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('lastEditTime', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('author', models.CharField(default='', max_length=30, verbose_name='作者')),
                ('authorInfo', models.TextField(default='', max_length=500, verbose_name='作者信息')),
                ('authorPhoto', models.ImageField(null=True, upload_to='book_img', verbose_name='作者照片')),
                ('translator', models.CharField(max_length=30, null=True, verbose_name='译者')),
                ('pressTime', models.DateTimeField(null=True, verbose_name='出版时间')),
                ('press', models.CharField(max_length=30, null=True, verbose_name='出版社')),
                ('page', models.IntegerField(default=0, verbose_name='页数')),
                ('price', models.IntegerField(default=99999, verbose_name='价格')),
                ('cover', models.ImageField(upload_to='book_img', verbose_name='封面')),
                ('score', models.FloatField(default=5, null=True, verbose_name='评分')),
            ],
            options={
                'verbose_name': '图书',
                'verbose_name_plural': '图书',
                'get_latest_by': 'lastEditTime',
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': '收藏管理',
                'verbose_name_plural': '收藏管理',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(choices=[(1, '1星'), (2, '2星'), (3, '3星'), (4, '4星'), (5, '5星')], default=0, verbose_name='评分')),
                ('content', models.CharField(max_length=200, verbose_name='内容')),
                ('createTime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('praise', models.IntegerField(default=0, verbose_name='赞数')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
                'get_latest_by': 'createTime',
            },
        ),
        migrations.CreateModel(
            name='FLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('labelName', models.CharField(max_length=10, verbose_name='标签名')),
            ],
            options={
                'verbose_name': '父标签',
                'verbose_name_plural': '父标签',
            },
        ),
        migrations.CreateModel(
            name='Praise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='praiseToComment', to='book.Comment', verbose_name='被赞评论')),
            ],
            options={
                'verbose_name': '评论点赞',
                'verbose_name_plural': '评论点赞',
            },
        ),
        migrations.CreateModel(
            name='SLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('labelName', models.CharField(max_length=10, verbose_name='标签名')),
                ('fatherLabel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.FLabel', verbose_name='父标签')),
            ],
            options={
                'verbose_name': '子标签',
                'verbose_name_plural': '子标签',
            },
        ),
    ]
