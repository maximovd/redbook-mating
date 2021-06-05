# Generated by Django 3.2 on 2021-04-25 21:35

from django.conf import settings
import django.contrib.gis.geos.point
from django.db import migrations, models
import django.db.models.deletion
import location_field.models.spatial
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=400)),
                ('location', location_field.models.spatial.LocationField(default=django.contrib.gis.geos.point.Point(1.0, 1.0), srid=4326)),
                ('phone', phone_field.models.PhoneField(blank=True, max_length=31)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]