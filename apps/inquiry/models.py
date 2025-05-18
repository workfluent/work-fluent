from django.db import models
from apps.core.abstracts.models import TimeStampedModel, UUIDModel, SoftDeleteModel

class Inquiry(TimeStampedModel, UUIDModel, SoftDeleteModel):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
