from django.contrib import admin

from vacancy.models import Vacancy


class VacancyAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'author',
        'title',
        'salary',
        'description',
        'profession',
        'exp_from',
        'exp_before',
        'created_at',
        'updated_at'
    )
    search_fields = (
        'author',
        'title',
        'salary',
        'description',
        'profession',
        'exp_from',
        'exp_before'
    )
    fields = (
        'author',
        'title',
        'salary',
        'description',
        'profession',
        'exp_from',
        'exp_before'
    )


admin.site.register(Vacancy, VacancyAdmin)
