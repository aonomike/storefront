from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class UpdateLog(models.Model):
    creation_date = models.DateTimeField(blank=False, null=False)
    created_by = models.ForeignKey(
        User, blank=False, null=False, on_delete=models.CASCADE
    )
    last_update_date = models.DateTimeField(blank=False, null=False)
    last_updated_by = models.ForeignKey(
        User, blank=False, null=False, on_delete=models.CASCADE
    )

    def save(self, *args, **kwargs):
        """On save, update timestamps"""
        if not self.id:
            self.creation_date = timezone.now()
        self.last_update_date = timezone.now()
        return super(UpdateLog, self).save(*args, **kwargs)
