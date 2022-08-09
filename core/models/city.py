from django.db import models
from .region import Region
from .content import Content


class City(models.Model):
    # reference to region
    region = models.ForeignKey(
        to=Region,
        null=True,
        on_delete=models.CASCADE,
    )
    content = models.ManyToManyField(Content)
    # Meta
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"city id{str(self.id)}"

    class Meta:
        indexes = [
            models.Index(fields=['region',]),
        ]