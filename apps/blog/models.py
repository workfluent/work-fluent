from django.db import models
from apps.core.abstracts.models import TimeStampedModel, UUIDModel, SlugModel, PublishableModel

class BlogPost(TimeStampedModel, UUIDModel, SlugModel, PublishableModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    article = models.TextField()

    def __str__(self):
        return self.title