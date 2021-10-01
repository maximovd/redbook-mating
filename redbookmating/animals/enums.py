from django.db import models


class Gender(models.TextChoices):
    MAN = 'M', 'M'
    WOMAN = 'W', 'W'
