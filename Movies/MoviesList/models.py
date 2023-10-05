from django.db import models
from django.contrib import auth

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=50,help_text="Publisher name")
    website = models.URLField(help_text="publisher website")
    email = models.EmailField()

    def __str__(self):
        return self.name

class Movies_Info(models.Model):
    name = models.CharField(max_length=100, help_text="Movie's name")
    date = models.DateField(verbose_name='Date the movie was released')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    contributors = models.ManyToManyField('Contributor', through="MovieContributor")

    def __str__(self):
        return self.name
    
class Contributor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(help_text="Contributor's email")

    def __str__(self):
        return self.last_name

class MovieContributor(models.Model):
    class ContributionRole(models.TextChoices):
        ACTOR = "ACTOR", "Actor"
        DIRECTOR = "DIRECTOR", "Director"
    movie = models.ForeignKey(Movies_Info, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    role = models.CharField(verbose_name="Contributor's role in this movie", choices=ContributionRole.choices, max_length=20)


class Review(models.Model):
    content = models.TextField()
    rating = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    creater = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies_Info, on_delete=models.CASCADE, help_text="Reviewed movie")

    def __str__(self):
        return f"Content: {self.content} \n By: {self.creater}"



