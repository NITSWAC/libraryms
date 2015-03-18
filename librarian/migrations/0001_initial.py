# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('authorid', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bookid', models.IntegerField(serialize=False, primary_key=True)),
                ('accno', models.IntegerField()),
                ('classno', models.CharField(max_length=100)),
                ('bookno', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('no_copies', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='bookauthor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('authorid', models.ForeignKey(to='librarian.Author')),
                ('bookid', models.ForeignKey(to='librarian.Book')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('issue_date', models.DateField()),
                ('due_date', models.DateField()),
                ('bookid', models.ForeignKey(to='librarian.Book')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('pubid', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('roll_number', models.CharField(unique=True, max_length=10, blank=True)),
                ('registration_number', models.CharField(unique=True, max_length=10, blank=True)),
                ('current_section', models.CharField(max_length=4)),
                ('current_year', models.CharField(max_length=4)),
                ('joining_year', models.CharField(max_length=4)),
                ('course', models.CharField(max_length=10)),
                ('branch', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=1)),
                ('email', models.CharField(unique=True, max_length=64)),
                ('birthday', models.DateField()),
                ('country', models.CharField(max_length=32)),
                ('mobile', models.CharField(max_length=16)),
                ('emergency_contact', models.CharField(max_length=16)),
                ('sbh_account', models.CharField(max_length=32, blank=True)),
                ('passport', models.CharField(max_length=20, blank=True)),
                ('hostel_room', models.CharField(max_length=10)),
                ('hostel', models.CharField(max_length=10)),
                ('mess', models.CharField(max_length=10)),
                ('created_location', models.CharField(max_length=32)),
                ('created_time', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='issue',
            name='userid',
            field=models.ForeignKey(to='librarian.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='pubid',
            field=models.ForeignKey(to='librarian.Publisher'),
            preserve_default=True,
        ),
    ]
