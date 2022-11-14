from django.db import models

# Create your models here.


class skill_model(models.Model):
    skill_name = models.CharField(max_length=100)
    skill_percentage = models.CharField(max_length=10)
    skill_progress_bar_color = models.CharField(max_length=50, null=True)