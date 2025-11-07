import time
import datetime
import os
from colorama import  Fore, Style

def mostrar_datos(data):
    #Limpia la pantalla en cada actualizacion (para que sea mas legible)
    os.system("cls" if os.name == "nt" else "clear")

    print("📊 Cotización del Dólar (actualizado en tiempo real)")
    print("-" * 50)
    for dolar in data:
        if "nombre" in dolar.keys() and "compra" in dolar.keys()  and "venta" in dolar.keys() :
            try:
                nombre = dolar["nombre"]
                compra = float(dolar["compra"])
                venta = float(dolar["venta"])
                print(
                    f"{Fore.BLUE}{nombre.ljust(25)}{Style.RESET_ALL}:" 
                    f"{Fore.RED}Compra {compra:,.2f}{Style.RESET_ALL} |"
                    f"{Fore.GREEN}Venta {venta:,.2f}{Style.RESET_ALL}"
                    
                )
            except(ValueError, TypeError):
                print(f"⚠️ No se pudo convertir los valores del {nombre}")   
        else:
            print("⚠️ Datos incompletos")
    print(f"\n⏰ {Fore.YELLOW}{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}{Style.RESET_ALL}")
    print("-" * 50)
    print("🔄 Actualizando en 10 segundos...\n")