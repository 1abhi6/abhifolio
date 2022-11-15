from django.contrib import admin
from myprojects.models import myprojects_model

# Register your models here.


class myproject_admin(admin.ModelAdmin):
    list_display = ['myprojects_title', 'myprojects_type',
                    'myprojects_lang', 'myprojects_desc','myprojects_link']


admin.site.register(myprojects_model, myproject_admin)
