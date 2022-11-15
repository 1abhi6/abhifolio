from django.contrib import admin
from contact.models import contact_model

# Register your models here.


class contact_admin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message']


admin.site.register(contact_model, contact_admin)
