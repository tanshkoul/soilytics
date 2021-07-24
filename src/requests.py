import requests
import os
from dotenv import load_dotenv
from html.parser import HTMLParser
# going to process the requests here

load_dotenv()

API_KEY = os.getenv('API_KEY')
# declare this as a local variable

BASEURL = 'https://api.ambeedata.com'

def getreq(URL, params):
    data = requests.get(URL)



