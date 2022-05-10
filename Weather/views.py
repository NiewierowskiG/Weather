from django.shortcuts import render
from django.shortcuts import HttpResponse
import requests
import folium


def home(request):
    if request.GET.get('submit'):
        url = 'http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={key}'
        city = request.GET.get('City')
        api_key = 'fcaf07b0c6e6a7745e7f4a0c49bd6fd9'
        api = requests.get(url.format(city=city, key=api_key)).json()
        try:
            map = folium.Map(width=400, height=400, location=[api['coord']['lat'], api['coord']['lon']], zoom_start=12)
        except KeyError:
            return render(request, 'Weather/LoadCity.html', {'error': True})
        map = map._repr_html_()
        weather = {
            "weather_desc": api['weather'][0]['description'],
            "temp": round((api['main']['temp'] - 32) * 5.0 / 9.0, 2), # convert Fahrenheit to Celsius
            "icon": f"http://openweathermap.org/img/w/{ api['weather'][0]['icon'] }.png",
            "city": city
        }
        return render(request, 'Weather/main.html', {'map': map, 'weather': weather})
    else:
        return render(request, 'Weather/LoadCity.html', {'error': False})