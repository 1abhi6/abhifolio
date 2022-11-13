from django.db import models
from tinymce.models import HTMLField
# Create your models here.


class about_model(models.Model):
    about_title = models.CharField(max_length=200)
    about_description = HTMLField()
    about_email = models.CharField(max_length=50)
    about_address = models.CharField(max_length=50)
    about_freelance = models.CharField(max_length=50)
    about_image = models.ImageField(
        upload_to="about_image", null=True, max_length=500, default=None)
    about_image_alt_text = models.CharField(max_length=200,default="Abhishek Gupta")
