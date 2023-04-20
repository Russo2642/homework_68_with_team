from django import forms
from vacancy.models import Vacancy
from vacancy.models import Application


class VacancyForm(forms.ModelForm):

    class Meta:
        model = Vacancy
        fields = (
            'title',
            'salary',
            'description',
            'profession',
            'exp_from',
            'exp_before'
        )

        labels = {
            'title': 'Название вакансии',
            'profession': 'Категория сферы деятельности',
            'salary': 'Уровень заработной платы (в тенге)',
            'description': 'Описание вакансии',
            'exp_from': 'Стаж от ',
            'exp_before':'Стаж до',
        }


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = (
            'applicant',
            'vacancy'
        )

        labels = {
            'applicant': 'Соискатель',
            'vacancy': 'Вакансия',
        }