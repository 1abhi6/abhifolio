from django.db import models

# Create your models here.


class header_model(models.Model):
    salutation_text = models.CharField(max_length=50, null=True)
    my_name = models.CharField(max_length=50, null=True)
    my_image = models.ImageField(
        upload_to="main_image", max_length=500, null=True, default=None)
    my_image_alt_text = models.CharField(max_length=200, null=True)
    my_skills = models.CharField(max_length=200, null=True)
