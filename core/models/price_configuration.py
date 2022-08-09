from django.db import models
from .content import Content


class PriceConfiguration(models.Model):
    """Price options for events"""

    content = models.ManyToManyField(Content)
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
