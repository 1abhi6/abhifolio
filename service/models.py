from django.db import models

# Create your models here.


class service_model(models.Model):
    service_title = models.CharField(max_length=50)
    service_description = models.TextField()
    service_icon = models.CharField(max_length=100)
