from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from security.models import UpdateLog


# Create your models here.
class Tag(UpdateLog):
    label = models.CharField(max_length=255)


class TaggedItem(UpdateLog):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField
    content_object = GenericForeignKey()