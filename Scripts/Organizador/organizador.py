import os
from datetime import date
from os import path
import pathlib
import json
import shutil

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
            
if __name__ == '__main__':
    # Primero limpiamos la pantalla
    os.system('cls')

    settings = Settings()

    # Asignación ruta que se va a escanear
    ruta = settings.config['ruta_escanear']

    # Crear el nombre que tendra la nueva carpeta 
    fecha_actual = f"{date.today().year}{date.today().month}{date.today().day}"
    ruta_nueva = os.path.join(ruta, fecha_actual)

    # Creación carpeta nueva
    if not os.path.isdir(ruta_nueva):
        os.mkdir(ruta_nueva)
        print(f"Se creó la carpeta {ruta_nueva}")

    # Creación carpeta Otros
    if not os.path.isdir(os.path.join(ruta_nueva, "Otros")):
            os.mkdir(os.path.join(ruta_nueva, "Otros"))
            print(f"Se creó la carpeta {os.path.join(ruta_nueva, 'Otros')}")

    # Creación carpetas para distribución de formatos
    for carpeta in settings.config['formatos']:
        if not os.path.isdir(os.path.join(ruta_nueva, carpeta)):
            os.mkdir(os.path.join(ruta_nueva, carpeta))
            print(f"Se creó la carpeta {os.path.join(ruta_nueva, carpeta)}")

    # Creamos una lista con los archivos y carpetas de la carpeta
    directorios = os.listdir(ruta)

    # Recorremos la lista de documentos
    for directorio in directorios:

        ruta_archivo_actual = os.path.join(ruta, directorio)

        # Validación que sean archivos 
        if os.path.isfile(ruta_archivo_actual):

            # Guardamos la extensión del archivo en una variable
            formato_actual = os.path.splitext(ruta_archivo_actual)[1].lower()

            formato_encontrado = False

            for nombre, formatos in settings.config['formatos'].items():

                if formato_actual in settings.config['formatos'][nombre]:
                    shutil.move(ruta_archivo_actual, os.path.join(ruta_nueva, nombre))
                    print(f"Se movio el archivo {directorio} a la carpeta {os.path.join(ruta_nueva, nombre)}")
                    formato_encontrado = True
                    break

            if not formato_encontrado:
                shutil.move(ruta_archivo_actual, os.path.join(ruta_nueva, 'Otros'))
                print(f"Se movio el archivo {directorio} a la carpeta {os.path.join(ruta_nueva, 'Otros')}")

    print("Finalizo el proceso")
