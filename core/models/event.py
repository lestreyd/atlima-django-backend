from django.db import models

from core.models.promo_code import PromoCode
from .country import Country
from .region import Region
from .city import City
from .sport import Sport
from .event_format import EventFormat
from .user import User
from .price_configuration import (
    PriceConfiguration,
)
from .organizer import Organizer
from .currency import Currency
from .notification import Notification
from .evsk import EventEVSKStatus
from .system import SystemObject
from .content import Content
from .event_property import EventProperty
from .slot import Slot
from .referee_slot import RefereeSlot
from .course import Course
from .team import Team


class Event(models.Model):
    """
    Event model for event representation in Atlima.
    Can be object with status Draft or Publish.
    Users can register to the event and participate
    in sport events with result checking and rating
    calculation.
    """

    photo = models.ImageField(upload_to="events")
    content = models.ManyToManyField(Content)
    properties = models.OneToOneField(
        EventProperty,
        on_delete=models.CASCADE
    )

    slots = models.ManyToManyField(Slot)
    referee_slots = models.ManyToManyField(
        RefereeSlot
    )
    courses = models.ManyToManyField(Course)

    address = models.CharField(
        max_length=4096, null=True, blank=True
    )
    start_event_date = models.DateTimeField(
        null=True, blank=True
    )
    end_event_date = models.DateTimeField(
        null=True, blank=True
    )

    country = models.ForeignKey(
        to=Country,
        on_delete=models.CASCADE,
        related_name="event_country",
        null=True,
        blank=True,
    )
    region = models.ForeignKey(
        to=Region,
        on_delete=models.CASCADE,
        related_name="event_region",
        null=True,
        blank=True,
    )

    city = models.ForeignKey(
        to=City,
        on_delete=models.CASCADE,
        related_name="event_city",
        null=True,
        blank=True,
    )
    sport_type = models.ForeignKey(
        to=Sport,
        related_name="event_sport_type",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    slug = models.SlugField(
        max_length=255,
        unique=True,
        null=True,
        blank=True,
    )

    site = models.CharField(
        max_length=512, null=True, blank=True
    )

    DRAFT = "Draft"
    PUBLISH = "Publish"
    DELETED = "Deleted"

    statuses = [
        (DRAFT, "DRAFT"),
        (PUBLISH, "PUBLISH"),
        (DELETED, "DELETED"),
    ]

    status = models.CharField(
        choices=statuses,
        max_length=32,
        default=DRAFT,
        null=True,
        blank=True,
    )

    format = models.ForeignKey(
        to=EventFormat,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="event_format",
    )

    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(auto_now=True)

    approved = models.BooleanField(default=False)

    organizer = models.ForeignKey(
        to=Organizer,
        related_name="event_organizer",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    registration_opened = models.BooleanField(
        default=False
    )
    price_option = models.ForeignKey(
        to=PriceConfiguration,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="event_price_option",
    )
    price = models.DecimalField(
        max_digits=17,
        decimal_places=2,
        default=0,
        null=True,
        blank=True,
    )
    currency = models.ForeignKey(
        to=Currency,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="currency_registration_price",
    )

    evsk = models.ForeignKey(
        to=EventEVSKStatus,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )
    standart_speed_courses = models.BooleanField(
        default=False
    )
    created_by = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="event_created_by",
    )

    phone = models.CharField(
        max_length=512, null=True, blank=True
    )
    email = models.EmailField(
        null=True, blank=True
    )

    completed = models.BooleanField(default=False)
    has_results = models.BooleanField(
        default=False
    )
    imported = models.BooleanField(default=False)
    dismissed = models.BooleanField(default=False)
    dismiss_reason = models.CharField(
        max_length=4096, null=True, blank=True
    )
    moderated = models.BooleanField(default=False)

    banned = models.BooleanField(
        default=None, null=True, blank=True
    )
    banned_moderation = models.BooleanField(
        default=False
    )

    freezed = models.BooleanField(default=False)

    first_calculation_datetime = (
        models.DateTimeField(
            null=True, blank=True
        )
    )
    last_calculation_datetime = (
        models.DateTimeField(
            null=True, blank=True
        )
    )

    director = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='director'
    )
    administrators = models.ManyToManyField(User, related_name='administrators')
    promocodes = models.ManyToManyField(PromoCode)
    teams = models.ManyToManyField(Team)

    def __str__(self):
        return self.slug or str(self.created)

    def delete(self, *args, **kwargs):
        notifications = Notification.objects.filter(
            object_type=SystemObject.objects.get(
                title="event", object_id=self.id
            )
        ).all()
        notifications.delete()

        super(Event, self).delete()
