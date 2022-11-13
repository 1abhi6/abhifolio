from django.contrib import admin
from service.models import service_model

# Register your models here.


class service_admin(admin.ModelAdmin):
    list_display = ['service_title', 'service_description', 'service_icon']


admin.site.register(service_model, service_admin)
