from django.contrib import admin
from myportfolio.models import myportfolio_model
# Register your models here.


class myportfolio_admin(admin.ModelAdmin):
    list_display = ['myportfolio_img_link', 'myportfolio_img',
                    'myportfolio_img_alt_text']


admin.site.register(myportfolio_model, myportfolio_admin)
