from django.db import models

# Create your models here.
class Movies_Info(models.Model):
    name = models.CharField(max_length=100, help_text="Movie's name")
    date = models.DateField(verbose_name='Date the movie was released')


