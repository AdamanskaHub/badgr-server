# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-11-02 21:38


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backpack', '0010_auto_20180802_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backpackcollection',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]
