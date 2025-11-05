import requests
import time
import os

url = "https://dolarapi.com/v1/dolares"

while True:
    try:
        #Limpia la pantalla en cada actualizacion (para que sea mas legible)
        os.system("cls" if os.name == "nt" else "clear") 

        print("📊 Cotización del Dólar (actualizado en tiempo real)")
        print("-" * 50)

        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        for dolar in data:
            nombre = dolar["nombre"]
            compra = dolar["compra"]
            venta = dolar["venta"]
            print(f"{nombre}: Compra {compra} | Venta {venta}")

        print("-" * 50)
        print("🔄 Actualizando en 10 segundos...\n")

    except requests.exceptions.RequestException as e:
        print("❌ Error al obtener los datos:", e)

    # Espera 10 segundos antes de volver a actualizar
    time.sleep(10)