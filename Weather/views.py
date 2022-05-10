from django.shortcuts import render
from django.shortcuts import HttpResponse
import requests


def home(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={key}'
    city = "Drohiczyn"
    api_key = 'fcaf07b0c6e6a7745e7f4a0c49bd6fd9'
    api = requests.get(url.format(city=city, key=api_key)).json()
    weather = {
        "weather_desc": api['weather'][0]['description'],
        "temp": (api['main']['temp'] - 32) * 5.0 / 9.0  # convert Fahrenheit to Celsius
    }
    return HttpResponse("eo")
