# Generated by Django 4.1.7 on 2023-04-17 11:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('DEVELOPMENT', 'Разработка'), ('DATASCIENCE', 'Наука о данных'), ('DATAENGINEER', 'Инженер данных'), ('DEVOPS', 'DevOps'), ('TESTER', 'Тестировщик'), ('OTHER', 'Другое')], default='OTHER', max_length=50, verbose_name='Категория')),
                ('title', models.CharField(max_length=500, verbose_name='Наименование')),
                ('email', models.EmailField(blank=True, max_length=254, unique=True, verbose_name='Электронная почта')),
                ('phone', models.CharField(max_length=15, verbose_name='Телефон')),
                ('salary', models.IntegerField(blank=True, null=True, verbose_name='Зарпалата')),
                ('date_birth', models.DateField(verbose_name='Дата рождения')),
                ('sex', models.CharField(choices=[('MALE', 'Мужской'), ('FEMALE', 'Женский'), ('OTHER', 'Другое')], default='OTHER', max_length=50, verbose_name='Пол')),
                ('marital_status', models.CharField(choices=[('MARRIED', 'Женат/Замужем'), ('SINGLE', 'Холост/а'), ('WIDOWED', 'Вдовец/Вдова'), ('DIVORCED', 'В разводе'), ('OTHER', 'Другое')], default='OTHER', max_length=50, verbose_name='Семейное положение')),
                ('address1', models.CharField(blank=True, max_length=200, null=True, verbose_name='Адрес 1')),
                ('address2', models.CharField(blank=True, max_length=200, null=True, verbose_name='Адрес 2')),
                ('city', models.CharField(choices=[('ALMATY', 'Алматы'), ('TARAZ', 'Тараз'), ('SHIMKENT', 'Шымкент'), ('ASTANA', 'Астана'), ('OTHER', 'Другое')], default='OTHER', max_length=50, verbose_name='Город')),
                ('telegram', models.URLField(max_length=300, verbose_name='Телеграм')),
                ('whatsapp', models.URLField(blank=True, max_length=300, null=True, verbose_name='Ватсап')),
                ('linkedin', models.URLField(blank=True, max_length=300, null=True, verbose_name='Линкедин')),
                ('facebook', models.URLField(blank=True, max_length=300, null=True, verbose_name='Фэйсбук')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cv', to=settings.AUTH_USER_MODEL, verbose_name='Соискатель')),
            ],
        ),
    ]
