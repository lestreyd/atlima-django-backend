from django.db import models
from .content import Content


class Course(models.Model):
    """Course model for :model:Event"""

    # номер упражнения для сквозной нумерации упражнений
    course_number = (
        models.PositiveSmallIntegerField()
    )
    content = models.ManyToManyField(Content)
    image = models.ImageField(upload_to="courses")
    # название
    title = models.CharField(max_length=256)
    # количество зачётных выстрелов
    scoring_shoots = (
        models.PositiveSmallIntegerField(
            null=True, blank=True
        )
    )
    # минимальное количество выстрелов
    minimum_shoots = (
        models.PositiveSmallIntegerField(
            null=True, blank=True
        )
    )
    # иллюстрация
    illustration = models.ImageField(
        upload_to="courses"
    )
    # зачётных выстрелов по картонным мишеням (при наличии картонных мишеней)
    scoring_paper = (
        models.PositiveSmallIntegerField(
            null=True, blank=True
        )
    )

    def __str__(self):
        return f"{self.title} (event id={self.event.id})"
