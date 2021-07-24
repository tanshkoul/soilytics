import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')

BASEURL = 'https://api.ambeedata.com'

endpt = '/soil/latest/by-lat-lng'

headers = {
    'x-api-key':API_KEY,
}

def getlatlng(lat: str, lng: str) -> dict:
    return {
        'lat':lat,
        'lng':lng
    }
    

def getreq(URL: str, query: dict, headers: dict) -> str:
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

    print(statuses[status])

    return data.text