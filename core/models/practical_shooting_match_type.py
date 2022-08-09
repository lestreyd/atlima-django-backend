from django.db import models
from .content import Content


class PracticalShootingMatchType(models.Model):
    """property for event""" ""

    content = models.ManyToManyField(Content)
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        sid = str(self.pk)
        return f"PropertyIPSC id{sid}"
