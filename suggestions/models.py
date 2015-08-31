from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import (
    GenericForeignKey)
from django.contrib.contenttypes.models import ContentType


class ObjectView(models.Model):

    """ Represents a user that viewed an object's page """
    user = models.ForeignKey(User)
    content_type = models.ForeignKey(ContentType, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:

        """ A pair of user,object is unique, to avoid duplication """
        unique_together = ('user', 'content_object',)


class ObjectViewDictionary(models.Model):

    """
    Represents an object that a user visited before visiting the current one
    """
    current_content_type = models.ForeignKey(ContentType, null=True)
    current_object_id = models.PositiveIntegerField(null=True)
    current_object = GenericForeignKey(
        'current_content_type', 'current_object_id')

    visited_before_content_type = models.ForeignKey(ContentType, null=True)
    visited_before_object_id = models.PositiveIntegerField(null=True)
    visited_before_object = GenericForeignKey(
        'visited_before_content_type', 'visited_before_object_id')

    visits = models.IntegerField(default=1)

    class Meta:
        unique_together = ('current_object', 'visited_before_object',)
