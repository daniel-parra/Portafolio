import os
from os import path
import pathlib
import json

class Settings():
    config = []
    NOMBRE_CONFIG = "settings.json"

    def __init__(self) -> None:
        try:
            ruta = ""
            if path.exists(path.join(os.getcwd(), self.NOMBRE_CONFIG)):
                ruta = path.join(os.getcwd(), self.NOMBRE_CONFIG)
            else:
                ruta = path.join(pathlib.Path(__file__).parent.absolute(), self.NOMBRE_CONFIG)

            with open(ruta, "r", encoding='utf-8-sig') as file:
                self.config = json.load(file)
        except Exception as e:
            print(e)
            
def definir_logitud_relleno(longitud_cadena, num_colum):
    try:
        if longitud_cadena > 10000:
            raise ValueError("La longitud del mensaje excede el permitido")
        elif longitud_cadena % num_colum == 0:
            return(longitud_cadena)
        else:
            multiplos = [numero for numero in range(0,10000) if numero % num_colum == 0 ]
            for i in multiplos:
                if i > longitud_cadena:
                    longitud_cadena = i
                    break
            return longitud_cadena
    except Exception as e:
        print(e)

def dividir_cadena(cadena, numero_caracteres):
    cadena_nueva = ""
    contador = 0
    for caracter in cadena:
        if contador == numero_caracteres:
            cadena_nueva += "-"
            contador = 0  
        contador += 1
        cadena_nueva += caracter
    return (cadena_nueva.split("-"))   


if __name__ == '__main__':
    os.system('cls')
    settings = Settings()
    with open(settings.config['archivo_mensaje'], mode='r', encoding='utf8') as fichero:
        contenido = fichero.readlines()
    mensaje = ""
    for i in contenido:
        mensaje += i.rstrip("\n")+" "

    numero_columnas = settings.config['numero_columnas']
    caracter_relleno = settings.config['caracter_relleno']

    longitud_rellenar = definir_logitud_relleno(len(mensaje), numero_columnas)

    cadena_cifrar = (mensaje.replace(' ',caracter_relleno).ljust(longitud_rellenar,caracter_relleno)).upper()

    cadena_cifrada = ""
    contador = 0
    x = dividir_cadena(cadena_cifrar, numero_columnas)
    while contador < numero_columnas:
        for i in x:
            cadena_cifrada += i[contador]
        contador += 1

    with open(settings.config['archivo_cifrado'], "w+") as archivo:
        archivo.write(cadena_cifrada)
