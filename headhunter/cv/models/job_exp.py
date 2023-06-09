from django.db import models

from cv.models import CV


class JobExperience(models.Model):
    cv = models.ForeignKey(
        to=CV,
        related_name='job_exp',
        null=False,
        blank=False,
        verbose_name='Резюме',
        on_delete=models.CASCADE
    )
    job_place = models.CharField(
        null=False,
        blank=False,
        max_length=500,
        verbose_name='Место работы'
    )
    job_exp = models.FloatField(
        null=False,
        blank=False,
        verbose_name='Стаж'
    )
    job_position = models.CharField(
        null=False,
        blank=False,
        max_length=500,
        verbose_name='Должность'
    )
    job_description = models.TextField(
        null=False,
        blank=False,
        max_length=3000,
        verbose_name='Обязанности'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время обновления"
    )
