from django.contrib.auth import get_user_model
from django.db import models
from cv.models.cv import CategoryChoice


class Vacancy(models.Model):
    author = models.ForeignKey(
        to=get_user_model(),
        verbose_name='Работодатель',
        related_name='vacancy',
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
    is_published = models.BooleanField(
        null=False,
        blank=False,
        default=False
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


class Message(models.Model):
    sender = models.ForeignKey(
        get_user_model(),
        related_name="sent_messages",
        on_delete=models.CASCADE,
    )
    recipient = models.ForeignKey(
        get_user_model(),
        related_name="received_messages",
        on_delete=models.CASCADE,
    )
    vacancy_id = models.PositiveIntegerField()
    applicant_id = models.PositiveIntegerField()
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} to {self.recipient}: {self.text}"

    class Meta:
        ordering = ["timestamp"]


