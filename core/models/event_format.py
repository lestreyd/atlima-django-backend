from django.db import models
from .content import Content


class EventFormat(models.Model):
    """Event format for representing in event common
    interface"""

    content = models.ManyToManyField(Content)
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        sid = self.pk
        return f"event format id{sid}"
