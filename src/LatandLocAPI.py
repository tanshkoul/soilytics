from geopy.geocoders import Nominatim
import requests
import soilreq as sq

geolocator = Nominatim(user_agent="geoapiExercises")
city = "Waterloo"
country = "Canada"

loc = geolocator.geocode(city + ',' + country)
response = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=hourly,daily,current,minutely,alerts&units=metric&appid=8e898272d24992aae37e208b729aaed9".format(loc.latitude,loc.longitude))
data=response.json()
print(f"Latitude is {data['lat']: 2.2f} and longitude is {data['lon']: 2.2f}")

querystring = {
    "lat":loc.latitude,
    "lng":loc.longitude,
    }

BASEURL = 'https://api.ambeedata.com'

ENDPT = '/soil/latest/by-lat-lng'

headers = {
    'x-api-key':sq.prepkey(),
    'Content-type': "application/json",
}

response2 = sq.getreq(BASEURL + ENDPT, querystring, headers)

print(response2['data'][0]['soil_temperature'], response2['data'][0]['soil_moisture'])