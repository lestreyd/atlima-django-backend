from django.db import models
from .country import Country
from .content import Content


class Region(models.Model):
    # reference to country
    country = models.ForeignKey(
        to=Country,
        on_delete=models.CASCADE,
        related_name="region_country_ref",
    )
    
    content = models.ManyToManyField(Content)

    code = models.CharField(
        max_length=5, null=True, blank=True
    )

    # Meta
    weight = models.SmallIntegerField(
        verbose_name="Region weight in list"
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
