from django.db import models
from .weapon import Weapon


class Division(models.Model):
    """модель дивизиона для дисциплин"""

    name = models.CharField(max_length=32)
    name_ru = models.CharField(
        max_length=32, blank=True, null=True
    )

    weapon = models.ForeignKey(
        to=Weapon, on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to="divisions",
        null=True,
        blank=True,
    )

    description_ru = models.CharField(
        max_length=64, null=True, blank=True
    )
    description_en = models.CharField(
        max_length=64, null=True, blank=True
    )

    can_be_minor = models.BooleanField(
        default=True
    )
    can_be_major = models.BooleanField(
        default=True
    )

    custom_style = models.BooleanField(
        default=False
    )

    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
