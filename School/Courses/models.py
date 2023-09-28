from django.db import models

# Create your models here.
class Courses_Info(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField(help_text='Course number represents the course ID')