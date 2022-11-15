from django.db import models

# Create your models here.


class myportfolio_model(models.Model):
    myportfolio_img_link = models.CharField(max_length=50, null=True)
    myportfolio_img = models.ImageField(
        upload_to="myportfolio_img", null=True, default=None, max_length=500)
    myportfolio_img_alt_text = models.CharField(
        max_length=200, null=True, default="portfolio")
