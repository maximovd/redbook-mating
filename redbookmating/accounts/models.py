from django.db import models
from django.contrib.gis.geos import Point
from django.contrib.auth.models import User
from location_field.models.spatial import LocationField
from phone_field import PhoneField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=400)
    location = LocationField(based_fields=['city'], zoom=7, default=Point(1.0, 1.0))
    phone = PhoneField(blank=True)

    def __str__(self):
        return self.user.email
