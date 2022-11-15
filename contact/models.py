from django.db import models

# Create your models here.


class contact_model(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    subject = models.TextField(null=True)
    message = models.TextField(null=True)
