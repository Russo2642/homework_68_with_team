from cv.models import CV
from django import forms


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
            'facebook',
            'work_place',
            'work_exp',
            'work_position',
            'work_description'
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
            'facebook': 'Facebook(ссылка)',
            'work_place': 'Место работы',
            'work_exp': 'Стаж',
            'work_position': 'Должность',
            'work_description': 'Обязанности'
        }
