
#Configuracion de variables globales del proyecto
from dotenv import load_dotenv
import os

load_dotenv() # Carga las variables del .env

API_URL = os.getenv("API_URL")
UPDATE_INTERVAL = int(os.getenv("UPDATE_INTERVAL", 10))