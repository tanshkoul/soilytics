from django import forms
from django.conf import settings
import requests
from geopy.geocoders import Nominatim
import datetime 

class AmbeeForm(forms.Form):
    city = forms.CharField(label="Enter the city:", 
                            required=True,
                            widget= forms.TextInput(attrs={'placeholder':'Enter the city'}))
    country = forms.CharField(label="Enter the country:", 
                                required=True,
                                widget= forms.TextInput(attrs={'placeholder':'Enter the country'}))

    def prepkey(api) -> str:
        
        API_KEY = settings.AMBEE_API_KEY
        return API_KEY 

    def getreq(form, URL: str, query: dict, headers: dict) -> str:
        data = requests.get(
            URL, 
            params=query,
            headers=headers
            )

        status = str(data.status_code)

        statuses = {
            '200':'all good',
            '299':'API doesn\'t support this',
            '401':'provide the API key!',
            '403':'API key lacks perms',
            '404':'resource doesn\'t exist',
            '429':'exceeded API call quota',
            '500':'servers not working man',
        }

        # use only if testing the application
        # print(statuses[status])
        # if status == '200':
        return data.json()
        # else:
        #     return "Wrong Input"

    def gather(self):    

        geolocator = Nominatim(user_agent="geoapiExercises")
        city = self.cleaned_data['city']
        country = self.cleaned_data['country']

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

        URL = 'https://api.ambeedata.com/soil/latest/by-lat-lng'

        headers = {
            'x-api-key': self.prepkey(),
            'Content-type': "application/json",
        }
        b=""
        today = datetime.date.today()   
        for i in range(7):
            b+=(f"Temperature in {city}, {country} on {today + datetime.timedelta(days = i) } is {data['daily'][i]['temp']['day']: .2f} degrees Celsius. There is {data['daily'][i]['weather'][0]['description']}?\n")

        bb = b.split('?')
        response2 = self.getreq(URL, querystring, headers)

        data2 = response2['data'][0]

        # b=(f"Soil temperature at {city}, {country} ({data['lat']: .2f}, {data['lon']: .2f}) is {data2['soil_temperature']: .2f} degrees Celsius.")
        c=(f"Soil moisture at the same location is {data2['soil_moisture']: .2f}%.")
        bb.insert(0, a)
        bb.insert(1, c)
        finalstring = bb
        return finalstring
