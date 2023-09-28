from django.shortcuts import render

# Create your views here.

def welcome_view(requst):
   myName = 'Abdulhamid'
   return render(requst, 'base.html', {'whatever': myName})
