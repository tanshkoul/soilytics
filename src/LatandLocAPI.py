import json
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")
city = "Agra"
country = "India"
loc = geolocator.geocode(city+',' + country)
import requests
response = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=hourly,daily,current,minutely,alerts&units=metric&appid=8e898272d24992aae37e208b729aaed9".format(loc.latitude,loc.longitude))
data=response.json()
print(data['lat'])
