import os
import time
from dotenv import load_dotenv
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




def obtener_lugares(df_munis, categorias, cantidad, token):

    municipios = df_munis[0:cantidad]
    
    url = "https://api.foursquare.com/v3/places/search?ll=41.086958%2C-3.624399&radius=2500&categories=16032%2C17114%2C13065%2C17031%2C11037&sort=DISTANCE&limit=10"

    headers = {
        "accept": "application/json",
        "Authorization": f"{token}"
    }

    response = requests.get(url, headers=headers)

    print(response.text)




def localizar(latlong, categoria, radio, maximo, ordenar, token):

    url = f"https://api.foursquare.com/v3/places/search?ll={latlong}&radius={radio}&categories={categoria}&sort={ordenar.upper()}&limit={maximo}"
    headers = {
    "Accept": "application/json",
    "Authorization": token
    }
    response = requests.request("GET", url, headers=headers)
    return response.json()

categorias = {
    16032 : 'Parques o areas verdes para rodajes exteriores',
    17114 : 'Centros comerciales',
    13065 : 'Bares o restaurantes',
    17031 : 'Tiendas de disfraces',
    11037 : 'Alquileres de equipos audiovisuales'
}