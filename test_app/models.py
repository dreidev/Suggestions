from django.db import models
from suggestions.models import ObjectViewDictionary, ObjectView
from django.contrib.contenttypes.fields import GenericRelation


class DummyModel(models.Model):
    name = models.CharField(max_length=100)
    suggestions = GenericRelation(ObjectViewDictionary)
    view = GenericRelation(ObjectView)
