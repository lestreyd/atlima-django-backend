from django.db import models
from .content import Content


class EmailTemplate(models.Model):
    """Template for Email"""

    template_name = models.CharField(
        max_length=256
    )
    description = models.TextField()
    content = models.ManyToManyField(Content)

    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.template_name
