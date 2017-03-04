# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-02 07:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_libs.models
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('calendarium', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('filer', '0007_auto_20161016_1055'),
        ('workplan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(verbose_name='Start date')),
                ('end', models.DateTimeField(verbose_name='End date')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('description', models.TextField(blank=True, max_length=2048, verbose_name='Description')),
                ('end_recurring_period', models.DateTimeField(blank=True, null=True, verbose_name='End of recurring')),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('slug', models.SlugField(blank=True, max_length=256, verbose_name='Slug')),
                ('color', django_libs.models.ColorField(max_length=6, verbose_name='Color')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parentss', to='calendarium.EventCategory', verbose_name='Parent')),
            ],
        ),
        migrations.CreateModel(
            name='EventRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField()),
                ('relation_type', models.CharField(blank=True, max_length=32, null=True, verbose_name='Relation type')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contenttype', to='contenttypes.ContentType')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workplan.Event', verbose_name='Event')),
            ],
        ),
        migrations.CreateModel(
            name='Occurrence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(verbose_name='Start date')),
                ('end', models.DateTimeField(verbose_name='End date')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('description', models.TextField(blank=True, max_length=2048, verbose_name='Description')),
                ('original_start', models.DateTimeField(verbose_name='Original start')),
                ('original_end', models.DateTimeField(verbose_name='Original end')),
                ('cancelled', models.BooleanField(default=False, verbose_name='Cancelled')),
                ('title', models.CharField(blank=True, max_length=256, verbose_name='Title')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='occurrencess', to=settings.AUTH_USER_MODEL, verbose_name='Created by')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='occurrencess', to='workplan.Event', verbose_name='Event')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='name')),
                ('description', models.TextField(verbose_name='description')),
                ('frequency', models.CharField(choices=[(b'YEARLY', 'Yearly'), (b'MONTHLY', 'Monthly'), (b'WEEKLY', 'Weekly'), (b'DAILY', 'Daily')], max_length=10, verbose_name='frequency')),
                ('params', models.TextField(blank=True, null=True, verbose_name='params')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eventss', to='workplan.EventCategory', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='event',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eventss', to=settings.AUTH_USER_MODEL, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='event',
            name='image',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='calendarium_event_imagess', to='filer.Image', verbose_name='Image'),
        ),
        migrations.AddField(
            model_name='event',
            name='rule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workplan.Rule', verbose_name='Rule'),
        ),
    ]
