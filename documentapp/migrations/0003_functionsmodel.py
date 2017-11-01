# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 03:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documentapp', '0002_auto_20171027_1743'),
    ]

    operations = [
        migrations.CreateModel(
            name='functionsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('functionName', models.CharField(default='', max_length=300)),
                ('functionDescription', models.CharField(default='', max_length=500)),
                ('fdocument', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documentapp.document')),
            ],
        ),
    ]
