# Generated by Django 4.1.7 on 2023-04-21 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0004_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='applicant_id',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='vacancy_id',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]