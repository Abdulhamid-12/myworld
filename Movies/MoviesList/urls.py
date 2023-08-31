from django.urls import path
from . import views

urlpatterns = [
    path('test01', views.welcome_page, name='welcome_page'),
    path('test02', views.movie_name, name='movie_name'),
    path('', views.movies_list, name='movies_list'),
]