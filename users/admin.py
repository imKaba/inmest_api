from django.contrib import admin
from .models import *
# Register your models here.


class IMUserAdmin(admin.ModelAdmin):
    list_display=('first_name', 'last_name', 'is_active', 'user_type', 'date_created')




admin.site.register(IMUser)
admin.site.register(Cohort)
admin.site.register(CohortMember)