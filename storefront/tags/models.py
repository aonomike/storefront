from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from security.models import SecurityBaseModel


# Create your models here.
class Tag(SecurityBaseModel):
    label = models.CharField(max_length=255)


class TaggedItem(SecurityBaseModel):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
