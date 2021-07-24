from  geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")
city ="Agra"
country ="India"
loc = geolocator.geocode(city+','+ country)
print("latitude is :-" ,loc.latitude,"\nlongtitude is:-" ,loc.longitude)