# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-12-11 09:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('isselect', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smallimg', models.CharField(max_length=50)),
                ('img', models.CharField(max_length=50)),
                ('packet', models.CharField(max_length=50)),
                ('information', models.CharField(max_length=256)),
                ('rated', models.CharField(max_length=256)),
                ('each', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('purchase', models.CharField(max_length=50)),
                ('act', models.CharField(max_length=50)),
                ('goodsid', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='GoodsDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goodid', models.CharField(max_length=20)),
                ('smallimg', models.CharField(max_length=50)),
                ('img', models.CharField(max_length=50)),
                ('img1', models.CharField(max_length=50)),
                ('packet', models.CharField(max_length=50)),
                ('information', models.CharField(max_length=256)),
                ('rated', models.CharField(max_length=256)),
                ('each', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('purchase', models.CharField(max_length=50)),
                ('act', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('addr', models.CharField(max_length=100)),
                ('pingjia', models.CharField(max_length=100)),
                ('shaidan', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('passwords', models.CharField(max_length=256)),
                ('tel', models.CharField(max_length=50)),
                ('token', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.AddField(
            model_name='cart',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP.GoodsDetail'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP.User'),
        ),
    ]
