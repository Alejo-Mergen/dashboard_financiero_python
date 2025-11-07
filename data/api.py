import requests

def obtener_datos_dolar(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data 
    except requests.exceptions.RequestException as e:
        print("❌ Error al obtener los datos:", e)
        return None