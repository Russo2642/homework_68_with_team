from django.contrib.auth import get_user_model
from django.db import models


class CategoryChoice(models.TextChoices):
    DEVELOPMENT = 'DEVELOPMENT', 'Разработка'
    DATASCIENCE = 'DATASCIENCE', 'Наука о данных'
    DATAENGINEER = 'DATAENGINEER', 'Инженер данных'
    DEVOPS = 'DEVOPS', 'DevOps'
    TESTER = 'TESTER', 'Тестировщик',
    OTHER = 'OTHER', 'Другое'


class CityChoice(models.TextChoices):
    ALMATY = 'ALMATY', 'Алматы'
    TARAZ = 'TARAZ', 'Тараз'
    SHIMKENT = 'SHIMKENT', 'Шымкент'
    ASTANA = 'ASTANA', 'Астана'
    OTHER = 'OTHER', 'Другое'


class SexChoice(models.TextChoices):
    MALE = 'MALE', 'Мужской'
    FEMALE = 'FEMALE', 'Женский'
    OTHER = 'OTHER', 'Другое'


class MaritalChoice(models.TextChoices):
    MARRIED = 'MARRIED', 'Женат/Замужем'
    SINGLE = 'SINGLE', 'Холост/а'
    WIDOWED = 'WIDOWED', 'Вдовец/Вдова'
    DIVORCED = 'DIVORCED', 'В разводе'
    OTHER = 'OTHER', 'Другое'


class CV(models.Model):
    user = models.ForeignKey(
        null=False,
        to=get_user_model(),
        related_name='cv',
        blank=False,
        verbose_name='Соискатель',
        on_delete=models.CASCADE
    )
    category = models.CharField(
        choices=CategoryChoice.choices,
        default=CategoryChoice.OTHER,
        max_length=50,
        verbose_name='Категория'
    )
    title = models.CharField(
        max_length=500,
        verbose_name='Наименование',
        null=False,
        blank=False
    )
    email = models.EmailField(
        verbose_name='Электронная почта',
        unique=True,
        blank=True,
    )
    phone = models.CharField(
        null=False,
        blank=False,
        max_length=15,
        verbose_name='Телефон'
    )
    salary = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Зарпалата'
    )
    date_birth = models.DateField(
        blank=False,
        null=False,
        verbose_name='Дата рождения'
    )
    sex = models.CharField(
        choices=SexChoice.choices,
        default=SexChoice.OTHER,
        max_length=50,
        verbose_name='Пол'
    )
    marital_status = models.CharField(
        choices=MaritalChoice.choices,
        default=MaritalChoice.OTHER,
        max_length=50,
        verbose_name='Семейное положение'
    )
    address1 = models.CharField(
        null=True,
        blank=True,
        max_length=200,
        verbose_name='Адрес 1'
    )
    address2 = models.CharField(
        null=True,
        blank=True,
        max_length=200,
        verbose_name='Адрес 2'
    )
    city = models.CharField(
        choices=CityChoice.choices,
        default=CityChoice.OTHER,
        max_length=50,
        verbose_name='Город'
    )
    telegram = models.URLField(
        null=False,
        blank=False,
        max_length=300,
        verbose_name='Телеграм'
    )
    whatsapp = models.URLField(
        null=True,
        blank=True,
        max_length=300,
        verbose_name='Ватсап'
    )
    linkedin = models.URLField(
        null=True,
        blank=True,
        max_length=300,
        verbose_name='Линкедин'
    )
    facebook = models.URLField(
        null=True,
        blank=True,
        max_length=300,
        verbose_name='Фэйсбук'
    )
    work_place = models.CharField(
        null=False,
        blank=False,
        max_length=500,
        verbose_name='Место работы'
    )
    work_exp = models.FloatField(
        null=False,
        blank=False,
        verbose_name='Стаж'
    )
    work_position = models.CharField(
        null=False,
        blank=False,
        max_length=500,
        verbose_name='Должность'
    )
    work_description = models.TextField(
        null=False,
        blank=False,
        max_length=3000,
        verbose_name='Обязанности'
    )
    is_published = models.BooleanField(
        null=False,
        blank=False,
        default=False
    )

    def __str__(self):
        return f"{self.user} - {self.title} - {self.category}"
