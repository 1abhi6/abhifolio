from django.db import models

# Create your models here.


class education_model(models.Model):
    education_course_title = models.CharField(max_length=100)
    education_course_collge = models.CharField(max_length=100)
    education_course_year = models.CharField(max_length=10)
    education_course_desc = models.TextField()
