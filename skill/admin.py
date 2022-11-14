from django.contrib import admin
from skill.models import skill_model

# Register your models here.

class skill_admin(admin.ModelAdmin):
    list_display=['skill_name','skill_percentage','skill_progress_bar_color']

admin.site.register(skill_model,skill_admin)
