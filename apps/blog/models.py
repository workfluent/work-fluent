from django.db import models
from apps.core.abstracts.models import TimeStampedModel, UUIDModel, SlugModel, PublishableModel

class Topic(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class BlogPost(TimeStampedModel, UUIDModel, SlugModel, PublishableModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    article = models.TextField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title