from django.shortcuts import render

# Create your views here.

def welcome_view(requst):
   return render(requst, 'welcome.html')
