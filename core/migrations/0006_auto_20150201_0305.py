# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0005_auto_20150201_0256'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('rating', models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'*'), (2, b'**'), (3, b'***'), (4, b'****'), (5, b'*****')])),
                ('location', models.ForeignKey(to='core.Location')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='location',
            name='rating',
        ),
    ]
