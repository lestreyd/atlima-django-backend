from django.db import models
from .user import User
from .invite import EventRefereeInvite


class RefereeSlot(models.Model):
    user = models.ForeignKey(
        to=User,
        related_name="user_referee_slot",
        on_delete=models.CASCADE,
        db_index=True,
    )
    role = models.IntegerField(
        choices=EventRefereeInvite.roles,
        default=EventRefereeInvite.REFEREE,
    )

    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(auto_now=True)