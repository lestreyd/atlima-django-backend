from django.db import models
from .system import SystemLanguage


class Content(models.Model):
    """MultilingualTextBlock stores multilingual information
    about object with language and text data"""

    language = models.ForeignKey(
        to=SystemLanguage,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    content = models.TextField()

    # meta timestamps
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title
