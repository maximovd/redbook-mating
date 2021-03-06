# Generated by Django 3.2.4 on 2021-09-28 11:36

import animals.models
from django.conf import settings
import django.contrib.gis.geos.point
from django.db import migrations, models
import django.db.models.deletion
import location_field.models.spatial


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.IntegerField(default=0, help_text='Object version, increment when the object was changed')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, help_text='Datetime object created')),
                ('created_by', models.CharField(blank=True, help_text='Who changed the object', max_length=255, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, db_index=True, help_text='Datetime object updated')),
                ('updated_by', models.CharField(blank=True, help_text='Who updated the object', max_length=255, null=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True, help_text='Datetime object deleted')),
                ('is_deleted', models.BooleanField(db_index=True, default=False, help_text='Flag for deleting an object', verbose_name='Deleted')),
                ('name', models.CharField(max_length=150, verbose_name='Name of property')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AnimalType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.IntegerField(default=0, help_text='Object version, increment when the object was changed')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, help_text='Datetime object created')),
                ('created_by', models.CharField(blank=True, help_text='Who changed the object', max_length=255, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, db_index=True, help_text='Datetime object updated')),
                ('updated_by', models.CharField(blank=True, help_text='Who updated the object', max_length=255, null=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True, help_text='Datetime object deleted')),
                ('is_deleted', models.BooleanField(db_index=True, default=False, help_text='Flag for deleting an object', verbose_name='Deleted')),
                ('name', models.CharField(max_length=150, verbose_name='Name of type')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.IntegerField(default=0, help_text='Object version, increment when the object was changed')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, help_text='Datetime object created')),
                ('created_by', models.CharField(blank=True, help_text='Who changed the object', max_length=255, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, db_index=True, help_text='Datetime object updated')),
                ('updated_by', models.CharField(blank=True, help_text='Who updated the object', max_length=255, null=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True, help_text='Datetime object deleted')),
                ('is_deleted', models.BooleanField(db_index=True, default=False, help_text='Flag for deleting an object', verbose_name='Deleted')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('lat_title', models.CharField(max_length=225, verbose_name='Latin Name')),
                ('image', models.ImageField(blank=True, max_length=1024, null=True, upload_to=animals.models.upload_to_images, verbose_name='Image')),
                ('gender', models.CharField(choices=[('M', 'M'), ('W', 'W')], max_length=1, verbose_name='Sex')),
                ('age', models.PositiveIntegerField(verbose_name='Age')),
                ('description', models.TextField(verbose_name='Description')),
                ('location', location_field.models.spatial.LocationField(default=django.contrib.gis.geos.point.Point(1.0, 1.0), srid=4326)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('properties', models.ManyToManyField(to='animals.AnimalProperty')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='animals.animaltype')),
            ],
            options={
                'verbose_name': 'animal',
                'verbose_name_plural': 'animals',
            },
        ),
    ]
