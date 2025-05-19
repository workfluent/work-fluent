from django.db import models
from django.core.exceptions import ValidationError
from apps.core.abstracts.models import TimeStampedModel, UUIDModel, SoftDeleteModel

class Inquiry(TimeStampedModel, UUIDModel, SoftDeleteModel):
    BUDGET_CHOICES = [
        ("Less than 10,000", "Less than 10,000"),
        ("Less than 20,000", "Less than 20,000"),
        ("Between 20,000 and 50,000", "Between 20,000 and 50,000"),
        ("More than 50,000", "More than 50,000"),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    company_name = models.CharField(max_length=255, blank=True, null=True)
    company_website = models.URLField(max_length=255, blank=True, null=True)
    budget = models.CharField(max_length=50, choices=BUDGET_CHOICES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # Enforce 200-word limit on the message field
        if len(self.message.split()) > 200:
            raise ValidationError("Message cannot exceed 200 words.")

    def __str__(self):
        return f"Inquiry from {self.name} ({self.email})"
