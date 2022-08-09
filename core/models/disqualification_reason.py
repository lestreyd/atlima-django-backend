from django.db import models
from .content import Content


class DisqualificationReason(models.Model):
    """Модель причин дисквалификации"""
    content = models.ManyToManyField(Content)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        sid = str(self.id)
        return f"Disqualification {sid}"

