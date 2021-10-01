import logging

from django.db import models
from django.core import serializers
from django.contrib.gis.geos import Point
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from crum import get_current_user
from location_field.models.spatial import LocationField

from animals.enums import Gender
from animals.managers import AllManager, BaseManager, OrderedManager

logger = logging.getLogger(__name__)


class BaseModel(models.Model):
    objects = BaseManager()
    ordered_objects = OrderedManager()
    objects_all = AllManager()

    version = models.IntegerField(
        default=0,
        help_text='Object version, increment when the object was changed'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        help_text='Datetime object created'
    )
    created_by = models.CharField(
        blank=True,
        null=True,
        max_length=255,
        help_text='Who changed the object'
    )
    updated_at = models.DateTimeField(
        auto_now_add=True, db_index=True, help_text='Datetime object updated'
    )
    updated_by = models.CharField(
        blank=True,
        null=True,
        max_length=255,
        help_text='Who updated the object'
    )
    deleted_at = models.DateTimeField(auto_now_add=True, help_text='Datetime object deleted')
    is_deleted = models.BooleanField(
        default=False,
        verbose_name=_('Deleted'),
        db_index=True,
        help_text='Flag for deleting an object'
    )

    class Meta:
        abstract = True

    @property
    def server_name(self):
        return '___server___'

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.deleted_by = get_current_user().id
        self.is_deleted = True
        self.save()
        logger.info(
            f'[DELETE] Object {self.__class__} with id={self.pk} was deleted by user'
            f' ({self.deleted_by}) at {self.deleted_at}'
        )

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        is_new = self._state.adding
        if is_new:
            self.created_by = (
                get_current_user().id if get_current_user() else self.server_name
            )
            self.created_by = timezone.now()
        else:
            self.updated_by = (
                get_current_user().id if get_current_user() else self.server_name
            )
            self.updated_at = timezone.now()
            self.version += 1
        result = super().save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields,
        )

        if is_new:
            logger.debug(
                f'[CREATE] Object {self.__class__} with id={self.pk} was'
                f' created by user ({self.created_by}) at {self.created_at}'
            )
        else:
            logger.debug(
                f'[UPDATE] Object {self.__class__} with id={self.pk} was'
                f' created by user ({self.updated_by}) at {self.updated_at}'
            )
        logger.debug(f'[VALUES] {serializers.serialize("json", [self])}')
        return result


class AnimalType(BaseModel):
    name = models.CharField(
        max_length=150, null=False, blank=False, verbose_name=_('Name of type'),
    )


class AnimalProperty(BaseModel):
    name = models.CharField(
        max_length=150, null=False, blank=False, verbose_name=_('Name of property'),
    )


def upload_to_images(instance, filename):
    return f'animal_images/{instance.id}/{filename}'


class Animal(BaseModel):
    name = models.CharField(
        max_length=100, null=False, blank=False, verbose_name=_('Name')
    )
    lat_title = models.CharField(
        max_length=225, null=False, blank=False, verbose_name=_('Latin Name')
    )
    image = models.ImageField(
        upload_to=upload_to_images, max_length=1024, null=True, blank=True, verbose_name=_('Image')
    )
    gender = models.CharField(
        max_length=1, choices=Gender.choices, verbose_name=_('Sex'), null=False
    )
    age = models.PositiveIntegerField(null=False, verbose_name=_('Age'))
    type = models.ForeignKey(AnimalType, null=True, on_delete=models.SET_NULL)
    properties = models.ManyToManyField(AnimalProperty)
    description = models.TextField(verbose_name=_('Description'))
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    location = LocationField(zoom=7, default=Point(1.0, 1.0))

    class Meta:
        verbose_name = _('animal')
        verbose_name_plural = _('animals')

    def __str__(self):
        return f'Animal {self.lat_title} (id={self.pk}) owner {self.owner})'
