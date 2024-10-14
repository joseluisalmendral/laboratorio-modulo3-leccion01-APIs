import time
import pandas as pd
from tqdm import tqdm
import geopy.geocoders
from geopy.geocoders import Nominatim
import requests

geopy.geocoders.options.default_user_agent = 'nombre_app'
geopy.geocoders.options.default_timeout = 7
geolocator = Nominatim()



def obtener_coordenadas(lista):
    resultado = {'municipio': [], 'latitud': [], 'longitud': []}

    for muni in tqdm(lista):
        try:
            localizacion = geolocator.geocode(muni)
            resultado['municipio'].append(localizacion[0].split(',')[0])
            resultado['latitud'].append(localizacion.latitude)
            resultado['longitud'].append(localizacion.longitude)
            time.sleep(0.3)
        except:
            print("Algo salio mal")

    
    return resultado




def obtener_lugares(df_munis, cantidad):

    municipios = df_munis[0:cantidad]
    
    url = "https://api.foursquare.com/v3/places/search?ll=41.086958%2C-3.624399&radius=2500&categories=16032%2C17114%2C13065%2C17031%2C11037&sort=DISTANCE&limit=10"

    headers = {
        "accept": "application/json",
        "Authorization": "fsq38eO5vnBpB/6sfSyaptYChY624DcCYqh6DlLcSJCemy0="
    }

    response = requests.get(url, headers=headers)

    print(response.text)