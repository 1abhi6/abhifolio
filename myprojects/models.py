from django.db import models

# Create your models here.


class myprojects_model(models.Model):
    myprojects_title = models.CharField(max_length=50)
    myprojects_type = models.CharField(max_length=50)
    myprojects_lang = models.CharField(max_length=50)
    myprojects_desc = models.TextField()
    myprojects_link = models.CharField(max_length=100, null=True)
