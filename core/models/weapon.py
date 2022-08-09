from django.db import models
from .content import Content


class Weapon(models.Model):
    """Weapon model for divisions"""

    content = models.ManyToManyField(Content)
    image = models.ImageField(upload_to="weapons")
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        sid = str(self.pk)
        return f"Weapon id{sid}"
