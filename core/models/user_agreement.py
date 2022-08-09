from .content import Content
from django.db import models


class UserAgreement(models.Model):
    """
    User Agreement model with content, title
    and description fields in content field
    """

    content = models.ManyToManyField(Content)
    document_version = models.IntegerField(
        null=False, blank=False
    )
    slug = models.SlugField(
        max_length=64, unique=True
    )
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return (
            f"{self.pk}_{self.document_version}"
        )
