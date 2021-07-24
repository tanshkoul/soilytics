import json
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")
city = "Agra"
country = "India"
loc = geolocator.geocode(city+',' + country)
import requests
response = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=hourly,daily,current,minutely,alerts&units=metric&appid=8e898272d24992aae37e208b729aaed9".format(loc.latitude,loc.longitude))
data=response.json()
print(data['lat'], data['lon'])

url = "https://api.ambeedata.com/soil/latest/by-lat-lng"
querystring = {"lat":loc.latitude,"lng":loc.longitude}
headers = {
    'x-api-key': "aadf1192c0064117c61926efb2631d12fecf66ba12cab4507257cda34b4ed941",
    'Content-type': "application/json"
    }
response2 = requests.request("GET", url, headers=headers, params=querystring)
data2=response2.json()
print(data2['data'][0]['soil_temperature'], data2['data'][0]['soil_moisture'])