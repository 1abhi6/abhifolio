from django.contrib import admin
from about.models import about_model

# Register your models here.


class about_admin(admin.ModelAdmin):
    list_display = ['about_title', 'about_description', 'about_email',
                    'about_address', 'about_freelance', 'about_image', 'about_image_alt_text']


admin.site.register(about_model, about_admin)
