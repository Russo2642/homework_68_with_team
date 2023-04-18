from django.contrib import admin

from cv.models import CV

from cv.models import JobExperience


class CVAdmin(admin.ModelAdmin):
    list_display = (
        'id',
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


class JobExpAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'job_place',
        'job_exp',
        'job_position',
        'job_description'
    )


admin.site.register(CV, CVAdmin)
admin.site.register(JobExperience, JobExpAdmin)
