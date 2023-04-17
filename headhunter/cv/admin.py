from django.contrib import admin

from cv.models import CV


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


admin.site.register(CV, CVAdmin)
