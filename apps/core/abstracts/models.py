from django.db import models
from django.utils import timezone
import uuid


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class StatusModel(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')

    class Meta:
        abstract = True


class OrderableModel(models.Model):
    order = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True
        ordering = ['order']


class UUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class SoftDeleteModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.is_deleted = False
        self.deleted_at = None
        self.save()

    class Meta:
        abstract = True


class SlugModel(models.Model):
    slug = models.SlugField(unique=True, max_length=255)

    class Meta:
        abstract = True


class SEOModel(models.Model):
    meta_keywords = models.CharField(max_length=255, blank=True)
    meta_description = models.TextField(blank=True)
    meta_title = models.CharField(max_length=255, blank=True)

    class Meta:
        abstract = True


class ArchivableModel(models.Model):
    archived_at = models.DateTimeField(null=True, blank=True)
    is_archived = models.BooleanField(default=False)

    class Meta:
        abstract = True


class SortableModel(models.Model):
    order = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True
        ordering = ['order']


class ImageModel(models.Model):
    alt_text = models.CharField(max_length=255, blank=True, help_text="Alternative text for the image")
    image = models.ImageField(upload_to='images/')

    class Meta:
        abstract = True


class PublishableModel(models.Model):
    published_at = models.DateTimeField(null=True, blank=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        abstract = True


class TaggableModel(models.Model):
    tags = models.CharField(max_length=255, blank=True, help_text="Comma-separated tags")

    class Meta:
        abstract = True


class UserStampedModel(models.Model):
    created_by = models.CharField(max_length=255, null=True, blank=True)
    updated_by = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        abstract = True