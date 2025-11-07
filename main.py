import requests
import time
import datetime
import os
from colorama import  Fore, Style
import config


url = config.API_URL

from ui.display import mostrar_datos

from data.api import obtener_datos_dolar
    
def datos_del_dolar():
    while True:
        data = obtener_datos_dolar(url)
        if data != None:
            mostrar_datos(data)
                # Espera 10 segundos antes de volver a actualizar
            time.sleep(config.UPDATE_INTERVAL)

datos_del_dolar()



