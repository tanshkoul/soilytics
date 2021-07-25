def gather(city,country):    
    from geopy.geocoders import Nominatim
    import requests
    import soilreq as sq

    geolocator = Nominatim(user_agent="geoapiExercises")


    loc = geolocator.geocode(city + ',' + country)
    response = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=hourly,daily,current,minutely,alerts&units=metric&appid=8e898272d24992aae37e208b729aaed9".format(loc.latitude,loc.longitude))
    data=response.json()

    a=(f"Latitude is {data['lat']: .2f} and longitude is {data['lon']: .2f}.")

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

    data2 = response2['data'][0]

    b=(f"Soil temperature at {city}, {country} ({data['lat']: .2f}, {data['lon']: .2f}) is {data2['soil_temperature']: .2f} degrees Celsius.")
    c=(f"Soil moisture at the same location is {data2['soil_moisture']: .2f}%.")
    s=a+"\n"+b+"\n"+c
    return s
