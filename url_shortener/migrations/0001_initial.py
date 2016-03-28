# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-28 20:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortURL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True, verbose_name='URL \xe0 r\xe9duire')),
                ('code', models.CharField(max_length=6, unique=True)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name="Date d'enregistrement")),
                ('pseudo', models.CharField(blank=True, max_length=255, null=True)),
                ('nb_acces', models.IntegerField(default=0, verbose_name="Nombre d'acc\xe8s \xe0 l'URL")),
            ],
        ),
    ]
