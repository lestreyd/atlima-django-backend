from django.db import models
from .system import SystemLanguage
from .course import Course


class Target(models.Model):
    """Target model for :model:TargetSet"""

    NS = "NS"
    A = "A"
    AC = "AC"
    ACD = "ACD"

    allowed_results = (
        (NS, "NS"),
        (A, "A"),
        (AC, "AC"),
        (ACD, "ACD"),
    )

    allowed_result = models.CharField(
        max_length=10,
        choices=allowed_results,
        default=ACD,
    )
    image = models.ImageField(
        upload_to="targets", null=True, blank=True
    )
    paper = models.BooleanField(default=False)

    def __str__(self):
        return f"Target id{str(self.id)}"


class TargetType(models.Model):
    language = models.ForeignKey(
        to=SystemLanguage,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=512)
    target_type = models.ForeignKey(
        to=Target, on_delete=models.CASCADE
    )

    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class TargetSet(models.Model):
    """Набор мишеней"""

    target_type = models.ForeignKey(
        to=Target,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    course_target_array = models.ForeignKey(
        to=Course, on_delete=models.CASCADE
    )
    # количество мишеней данного типа
    amount = models.PositiveSmallIntegerField()
    # Стоимость Альфа: может быть 5, 10 и 15 в зависимости от сложности выстрела
    alpha_cost = models.PositiveSmallIntegerField(
        null=True, blank=True
    )

    def __str__(self):
        id = str(self.id)
        return f"target_type_{id}"
