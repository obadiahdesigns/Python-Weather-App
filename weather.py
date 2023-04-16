import requests
from pprint import pprint

API_Key = 'af9d25fc1faa4dd673d8a4704f7bdd5c'

city = input("Enter a city: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + API_Key + "&q=" +city

weather_data = requests.get(base_url).json()

# pprint is prettier print - it organizes data in a structured form
pprint(weather_data)


