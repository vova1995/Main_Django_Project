# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-09 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_userprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.FileField(upload_to='app_images'),
        ),
    ]