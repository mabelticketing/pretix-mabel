# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-09 16:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pretix_mabel', '0004_auto_20180109_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketlimit',
            name='item',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pretixbase.Item'),
        ),
    ]