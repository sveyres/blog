# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-11 11:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20170511_1059'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=20, verbose_name='Label')),
            ],
            options={
                'verbose_name': 'Cat\xe9gorie',
            },
        ),
    ]