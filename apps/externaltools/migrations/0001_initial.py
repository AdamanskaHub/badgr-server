# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-02-07 16:46


from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExternalTool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity_version', models.PositiveIntegerField(default=1)),
                ('entity_id', models.CharField(default=None, max_length=254, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=254)),
                ('description', models.CharField(blank=True, max_length=254, null=True)),
                ('xml_config', models.TextField()),
                ('config_url', models.URLField(blank=True, null=True)),
                ('client_id', models.CharField(blank=True, max_length=254, null=True)),
                ('client_secret', models.CharField(blank=True, max_length=254, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ExternalToolLaunchpoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('launchpoint', models.CharField(max_length=254)),
                ('launch_url', models.URLField()),
                ('label', models.CharField(max_length=254)),
                ('icon_url', models.URLField(blank=True, null=True)),
                ('externaltool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='externaltools.ExternalTool')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]