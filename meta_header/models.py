from django.db import models

# Create your models here.


class meta_header_model(models.Model):
    meta_header_title = models.CharField(max_length=50)
    meta_header_keyword = models.CharField(max_length=100)
    meta_header_description = models.TextField()
    meta_header_favicon = models.ImageField(
        upload_to="meta_header_favicon", max_length=500, null=True, default=None)

