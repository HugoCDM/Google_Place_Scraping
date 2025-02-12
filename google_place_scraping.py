import requests
import pandas as pd
from geopy.geocoders import Nominatim
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')

places = []
start = 0

your_address = input("What's yours address(Street and City)? ")
search = input('What do you like to search? ')

geolocator = Nominatim(user_agent='ny_explorer')
location = geolocator.geocode(your_address)
coordinates = f'@{location.latitude},{location.longitude},15z'

while True:
    try:
        params = {
            'engine': 'google_maps',
            'q': search,
            'api_key': api_key,
            'type': 'search',
            'start': start,
            'll': coordinates
        }

        response = requests.get('https://serpapi.com/search', params)
        search_results = response.json()['local_results']

        for place in search_results:
            title = place.get('title', '')
            address = place.get('address', '')
            phone = place.get('phone', '')
            rating = f"{place.get('rating', '')}★"

            places.append([title, address, phone, rating])

            start += 20

    except KeyError:
        break

df = pd.DataFrame(places, columns=['Place', 'Address', 'Phone', 'Rating'])
df = df.drop_duplicates()

df.to_excel('places.xlsx', index=False)
