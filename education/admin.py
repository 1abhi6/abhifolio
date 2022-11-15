from django.contrib import admin
from education.models import education_model
# Register your models here.


class education_admin(admin.ModelAdmin):
    list_display = ['education_course_title', 'education_course_college',
                    'education_course_year', 'education_course_desc']


admin.site.register(education_model, education_admin)
