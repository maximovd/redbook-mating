from django.db import models


class BaseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(is_deleted=False)


class AllManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter()


class OrderedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(is_deleted=False).order_by('-id')
