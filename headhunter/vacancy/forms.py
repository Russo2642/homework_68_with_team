from django import forms

from vacancy.models import Vacancy


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
            'title': 'Название предпочитаемой должности*',
            'profession': 'Категория сферы деятельности',
            'salary': 'Уровень заработной платы (в тенге)',
            'description': 'Описание вакансии',
            'exp_from': 'Стаж от ',
            'exp_before':'Стаж до',
        }