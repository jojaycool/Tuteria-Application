from django.db import models

from unobase import models as unobase_models


class Employee(models.Model):
    position = models.CharField(max_length=255)

    class Meta:
        abstract = True


class BoardMember(unobase_models.ContentModel, unobase_models.StateModel, Employee):
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']


class Executive(unobase_models.ContentModel, unobase_models.StateModel, Employee):
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
