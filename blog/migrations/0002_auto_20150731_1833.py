# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='posts',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
    ]
