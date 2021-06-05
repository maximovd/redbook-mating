from django.conf import settings
from django.db import models


def is_external_url(url):
    if url.startswith('https://') or url.startswith('http://'):
        return True
    return False


def get_full_media_url(image_field: models.ImageField):
    if not image_field:
        return None
    url = str(image_field)
    if is_external_url(url):
        return url
    return f'{settings.BASE_URL}{settings.MEDIA_URL}{url}'


def get_animal_image(obj):
    return get_full_media_url(obj.image)
