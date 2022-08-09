from django.db import models


class EventEVSKStatus(models.Model):
    """evsk model for :model:Event"""

    name = models.CharField(max_length=256)

    REGIONAL = 1
    FEDERAL = 2
    regional_statuses = [
        (REGIONAL, "Regional"),
        (FEDERAL, "Federal"),
    ]
    regional_status = models.IntegerField(
        choices=regional_statuses,
        default=1,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name
