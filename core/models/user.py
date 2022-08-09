from django.db import models
from django.contrib.auth.models import (
    AbstractUser,
)
import datetime
from dataclasses import dataclass, field
from .qualification import OfficialQualification
# from .city import City
# from .region import Region
# from .country import Country
from .privacy_settings import PrivacySetting


@dataclass
class Profile:
    """Dataclass Profile representing a user
    with custom fields for participating in
    sport events"""

    id: int
    first_name: str
    last_name: str
    email: str
    password: str
    phone_number: str
    native_first_name: str
    native_last_name: str
    country: int
    region: int
    city: int
    photo: bytes
    sex: str
    birth_date: datetime.date
    slug: str
    vk_profile: str
    fb_profile: str
    instagram: str
    strong_hand: str
    active: bool = field(init=True)
    qualifications: list[int] = field(
        default_factory=list
    )


class User(AbstractUser):
    """Atlima User model for representing
    a user in system"""

    # section for latin names
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True, blank=True)

    # native names are here
    native_first_name = models.CharField(
        max_length=255, null=True, blank=True
    )
    native_last_name = models.CharField(
        max_length=255, null=True, blank=True
    )
    native_middle_name = models.CharField(
        max_length=255, null=True, blank=True
    )

    # some contact information here
    email = models.EmailField(
        max_length=255, db_index=True, unique=True
    )
    phone_number = models.CharField(
        max_length=255,
        db_index=True,
        null=True,
        blank=True
    )
    facebook = models.CharField(max_length=255, null=True, blank=True)
    vk = models.CharField(max_length=255, null=True, blank=True)
    instagram = models.CharField(max_length=255, null=True, blank=True)

    password = models.CharField(max_length=255)

    # location information here
    country = models.ForeignKey('core.Country', on_delete=models.CASCADE, null=True, blank=True)
    region = models.ForeignKey('core.Region', on_delete=models.CASCADE, null=True, blank=True)
    city = models.ForeignKey('core.City', on_delete=models.CASCADE, null=True, blank=True)

    # photo now stored in model
    photo = models.ImageField(
        upload_to="profiles",
        null=True, blank=True
    )

    M, F = 1, 2
    sexes = [(M, "Male"), (F, "Female")]

    sex = models.IntegerField(
        choices=sexes, default=M
    )
    birth_date = models.DateField(
        blank=True, null=True
    )
    slug = models.SlugField(
        null=True, blank=True,
        db_index=True
    )

    R, L = 1, 2
    hands = [(R, "Right"), (L, "Left")]

    strong_hand = models.IntegerField(
        choices=hands, default=R
    )

    qualifications = models.ManyToManyField(
        OfficialQualification
    )

    privacy = models.OneToOneField(
        PrivacySetting,
        on_delete = models.CASCADE
    )

    def __str__(self):
        return (
            f"{self.last_name} {self.first_name}"
        )
