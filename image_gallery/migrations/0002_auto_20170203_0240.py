# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 02:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('image_gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='image_gallery_galleryplugin', serialize=False, to='cms.CMSPlugin'),
        ),
    ]
