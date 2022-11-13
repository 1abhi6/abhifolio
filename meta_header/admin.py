from django.contrib import admin
from meta_header.models import meta_header_model

# Register your models here.


class meta_header_admin(admin.ModelAdmin):
    display_items = ['meta_header_title', 'meta_header_keyword',
                     'meta_header_description', 'meta_header_favicon']


admin.site.register(meta_header_model, meta_header_admin)
