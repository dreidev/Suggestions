# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ObjectView',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField(null=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ObjectViewDictionary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('current_object_id', models.PositiveIntegerField(null=True)),
                ('visited_before_object_id', models.PositiveIntegerField(null=True)),
                ('visits', models.IntegerField(default=1)),
                ('current_content_type', models.ForeignKey(related_name='current_obj', to='contenttypes.ContentType', null=True)),
                ('visited_before_content_type', models.ForeignKey(to='contenttypes.ContentType', null=True)),
            ],
        ),
    ]
