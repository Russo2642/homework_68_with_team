from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):
    email = models.EmailField(
        verbose_name='Электронная почта',
        unique=True,
        blank=True
    )
    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to='user_pic',
        verbose_name='Аватар'
    )
    phone = models.CharField(
        null=True,
        blank=True,
        max_length=15,
        verbose_name='Телефон'
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
