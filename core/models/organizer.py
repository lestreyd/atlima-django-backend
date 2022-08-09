from .user import User
from django.db import models
from .country import Country
from .region import Region
from .city import City
from .content import Content


class Organizer(models.Model):
    """
    Organizer model for events. User
    with organizer role can create
    new event
    """

    image = models.ImageField(
        upload_to="organizers"
    )
    content = models.ManyToManyField(Content)
    slug = models.SlugField(
        max_length=255, unique=True
    )
    site = models.URLField()
    country = models.ForeignKey(
        to=Country,
        related_name="organizer_country",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    region = models.ForeignKey(
        to=Region,
        related_name="organizer_region",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    city = models.ForeignKey(
        to=City,
        related_name="organizer_city",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    address = models.TextField()
    phone = models.CharField(
        max_length=256, null=True, blank=True
    )
    email = models.EmailField(
        null=True, blank=True
    )
    imported = models.BooleanField(default=False)
    administrators = models.ManyToManyField(User)

    def __str__(self):
        sid = str(self.pk)
        return f"organizer id{sid}"
