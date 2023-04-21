from django import forms
from cv.models import CV
from cv.models import JobExperience


class CVForm(forms.ModelForm):
    phone = forms.RegexField(
        regex=r'[^\+?1?\d{9,15}$]',
        error_messages=({'invalid': 'Введите номер телефона в формате +7 777 123 4567. Максимум 15 цифр.'}),
    )

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
            'salary': 'Уровень заработной платы (в тенге)',
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
        widgets = {
            'date_birth': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       }),
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
            'job_exp': 'Стаж (лет)',
            'job_position': 'Должность',
            'job_description': 'Обязанности'
        }
