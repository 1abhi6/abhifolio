from django.contrib import admin
from header.models import header_model
# Register your models here.

class header_admin(admin.ModelAdmin):
    list_display=['salutation_text','my_name','my_image','my_image_alt_text']

admin.site.register(header_model,header_admin)
