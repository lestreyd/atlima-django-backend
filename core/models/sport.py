from django.db import models
# from .country import Country
# from .region import Region
# from .user import User


class Sport(models.Model):
    """Sport model for sport representation"""

    image = models.ImageField(upload_to="sports")
    slug = models.SlugField(
        max_length=255, unique=True
    )
    site = models.CharField(
        max_length=1024, null=True, blank=True
    )

    moderated = models.BooleanField(
        default=False,
        verbose_name="Events must be moderated",
    )

    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"sport {str(self.id)}"


class SportAdministrator(models.Model):
    sport = models.ForeignKey(
        to=Sport,
        on_delete=models.CASCADE,
        db_index=True,
        verbose_name="sport",
    )
    country = models.ForeignKey(
        'core.Country',
        on_delete=models.CASCADE,
        verbose_name="country",
    )
    region = models.ForeignKey(
        'core.Region',
        on_delete=models.CASCADE,
        verbose_name="region",
        null=True,
        blank=True,
    )
    user = models.ForeignKey(
        'core.User',
        on_delete=models.CASCADE,
        db_index=True,
        verbose_name="user",
    )
    # член СКС
    is_sks_member = models.BooleanField(
        default=False
    )
    # председатель СКС
    is_sks_president = models.BooleanField(
        default=False
    )
    # член коллегии судей
    is_referee_collegium_member = (
        models.BooleanField(default=False)
    )
    # председатель коллегии судей
    is_referee_collegium_president = (
        models.BooleanField(default=False)
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            f"{self.user.last_name} {self.user.first_name} - {self.sport.id}"
            or ""
        )