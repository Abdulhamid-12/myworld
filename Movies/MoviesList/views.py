from django.http import HttpResponse
from django.shortcuts import render
from .models import Movies_Info

import logging

logging.basicConfig(filename='scraper.log', level=logging.DEBUG,
                    format='%(asctime)s - %(message)s' , datefmt='%d-%b-%y %H:%M')

def movie_name(request):
    variable = 'Harry Potter'
    return render(request, 'base.html', {'variable': variable})

def welcome_page(request):
    message = f"<h1> Welcome to the Movies App! </h1> \n <p>The app has {Movies_Info.objects.count()} moviess</p>"
    return HttpResponse(message)

def movies_list(request):
    moviesObj = Movies_Info.objects.all()
    movies_list = []
    for movie in moviesObj:
        movies_list.append({'Movie': movie})

    context = {'movies_list': movies_list}
    return render(request, 'movies_list.html', context)
