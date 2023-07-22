from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User


from security.models import SecurityBaseModel


class LikedItem(SecurityBaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liked_item_user")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
