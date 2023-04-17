from django import forms

from cv.models import CV

from cv.models.cv import JobExperience


class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = (
            'title',
            'category',
            'salary',
            'email',
            'phone',
            'date_birth',
            'sex',
            'marital_status',
            'address1',
            'address2',
            'city',
            'telegram',
            'whatsapp',
            'linkedin',
            'facebook'
        )
        labels = {
            'title': 'Название предпочитаемой должности*',
            'category': 'Категория сферы деятельности',
            'salary': 'Уровень заработной платы',
            'email': 'Электронная почта*',
            'phone': 'Номер телефона*',
            'date_birth': 'Дата рождения*',
            'sex': 'Пол',
            'marital_status': 'Семейное положение',
            'address1': 'Адрес 1',
            'address2': 'Адрес 2',
            'city': 'Город проживания*',
            'telegram': 'Telegram(ссылка)*',
            'whatsapp': 'Whatsapp(ссылка)',
            'linkedin': 'LinkedIn(ссылка)',
            'facebook': 'Facebook(ссылка)'
        }


class JobExpForm(forms.ModelForm):
    class Meta:
        model = JobExperience
        fields = (
            'job_place',
            'job_exp',
            'job_position',
            'job_description'
        )
        labels = {
            'job_place': 'Место работы',
            'job_exp': 'Стаж',
            'job_position': 'Должность',
            'job_description': 'Обязанности'
        }