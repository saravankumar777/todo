# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-03 09:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workplan', '0003_auto_20170303_0909'),
    ]

    operations = [
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hdate', models.DateField()),
            ],
        ),
    ]
