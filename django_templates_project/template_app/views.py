from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.

def index(request):
    return render(request, "template_app/first.html")

def weather_view(request):
    weather_dictionary = {
        "istanbul"     : "30",
        "newyork"      : "36",
        "paris"        : [5,14,20,21],
        "rome"         : {"morning" : 15, "evening" : 18},
        "user_premium" : True,
        "test"         : "test test test test"
        }
    return render(request,"template_app/weather.html", context=weather_dictionary)