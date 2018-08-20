'''
#created for location search python script
#created by 'Ankit Nema'
here I have installed module 'requests' in my project folder
python -m pip install requests
then I have added json module
'''
import sys
import webbrowser
import json
import requests

URL = "http://maps.googleapis.com/maps/api/geocode/json"

location = "IBM, Pune"

parameters = {'address':location}

r = requests.get(url = URL, params = parameters)

content = r.json()

latitude = content['results'][0]['geometry']['location']['lat']
longitude = content['results'][0]['geometry']['location']['lng']
formatted_address = content['results'][0]['formatted_address']
print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"%(latitude, longitude,formatted_address))