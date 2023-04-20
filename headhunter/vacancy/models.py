from django.contrib.auth import get_user_model
from django.db import models
from cv.models.cv import CategoryChoice


class Vacancy(models.Model):
    author = models.ForeignKey(
        to=get_user_model(),
        verbose_name='Работодатель',
        related_name='employer',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    title = models.CharField(
        verbose_name='Вакансия',
        max_length=100,
        null=False,
        blank=False
    )
    salary = models.DecimalField(
        verbose_name='Заработная плата',
        max_digits=12,
        decimal_places=2,
        null=False,
        blank=False
    )
    description = models.TextField(
        verbose_name='Описание вакансии',
        null=True
    )
    profession = models.CharField(
        verbose_name='Сфера деятельности',
        max_length=30,
        null=False,
        blank=False,
        choices=CategoryChoice.choices,
        default=CategoryChoice.OTHER

    )
    exp_from = models.IntegerField(
        verbose_name='Стаж от',
        null=False,
        blank=False
    )
    exp_before = models.IntegerField(
        verbose_name='Стаж до',
        null=False,
        blank=False
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата редактирования',
        auto_now=True
    )

    class Meta:
        verbose_name = 'Vacancy'


class Application(models.Model):
    applicant = models.ForeignKey(
        to=get_user_model(),
        verbose_name='Соискатель',
        related_name='applications',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    vacancy = models.ForeignKey(
        to=Vacancy,
        verbose_name='Вакансия',
        related_name='applications',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата редактирования',
        auto_now=True
    )

    class Meta:
        verbose_name = 'Application'



