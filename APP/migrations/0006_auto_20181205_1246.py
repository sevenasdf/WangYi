# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-12-05 12:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0005_goodsdetail_img1'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodsdetail',
            name='addr',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='goodsdetail',
            name='city',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='goodsdetail',
            name='pingjia',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='goodsdetail',
            name='shaidan',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='goodsdetail',
            name='time',
            field=models.CharField(default='', max_length=100),
        ),
    ]