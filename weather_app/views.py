from django.shortcuts import render
from django import template

# Create your views here.

import requests

def index(request):
    # https://openweathermap.org/  --Create an account here to get the api key
    # url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=API_KEY' -- we have to give the API_KEY
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=94f6e1690c4489629c2c4f325bc7610a'

    city1 = 'Shimoga'
    city2 = 'Pune'
    city3 = 'Bengaluru'


    city1_weather = requests.get(url.format(city1)).json() #we are requesting the API data and converting the JSON to Python data types
    city2_weather = requests.get(url.format(city2)).json() #we are requesting the API data and converting the JSON to Python data types
    city3_weather = requests.get(url.format(city3)).json() #we are requesting the API data and converting the JSON to Python data types
    
    print(city1_weather) #checking the output
    print(city2_weather) #checking the output
    print(city3_weather) #checking the output

    weather1 = {
        'city1' : city1,
        'temperature' : city1_weather['main']['temp'],
        'description' : city1_weather['weather'][0]['description'],
        'icon' : city1_weather['weather'][0]['icon'],
        'max_temp': city1_weather['main']['temp_max'],
        'max_min': city1_weather['main']['temp_min'],
        'humidity': city1_weather['main']['humidity']
    }
    weather2 = {
        'city2' : city2,
        'temperature' : city2_weather['main']['temp'],
        'description' : city2_weather['weather'][0]['description'],
        'icon' : city2_weather['weather'][0]['icon'],
        'max_temp': city2_weather['main']['temp_max'],
        'max_min': city2_weather['main']['temp_min'],
        'humidity': city2_weather['main']['humidity']
    }
    weather3 = {
        'city3' : city3,
        'temperature' : city3_weather['main']['temp'],
        'description' : city3_weather['weather'][0]['description'],
        'icon' : city3_weather['weather'][0]['icon'],
        'max_temp': city3_weather['main']['temp_max'],
        'max_min': city3_weather['main']['temp_min'],
        'humidity': city3_weather['main']['humidity']
    }



    return render(request, 'index.html', {'weather1' : weather1,'weather2':weather2,'weather3':weather3}) #returns the index.html template
