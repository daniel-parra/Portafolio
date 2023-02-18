import os
from datetime import date
import shutil

if __name__ == '__main__':
    # Primero limpiamos la pantalla
    os.system('cls')

    # Asigamos la ruta 
    ruta = r'ruta'

    """
        Creamos lista con los formatos esperados para validar
    """
    formatos_documento = [".pdf", ".txt", '.pptx', '.docx', '.xls', '.epub']
    formatos_video = ['.mp4', '.avi']
    formatos_imagen = ['.jpeg', '.svg', '.png', '.jpg']
    formatos_audio = ['.mp3']
    
    # Crear el nombre que tendra la nueva carpeta 
    fecha_actual = f"{date.today().year}{date.today().month}{date.today().day}"
    ruta_nueva = os.path.join(ruta, fecha_actual)

    # Creamos una lista con los nombres de las carpetas que se van a crear 
    carpetas = ["Documentos", "Video", "Audio", "Imagen", "Otros"]

    # Creamos la carpeta raiz
    if not os.path.isdir(ruta_nueva):
        os.mkdir(ruta_nueva)

    # Creamos las carpetas donde se moveran los archivos despues de clasificados
    for carpeta in carpetas:
        if not os.path.isdir(os.path.join(ruta_nueva, carpeta)):
            os.mkdir(os.path.join(ruta_nueva, carpeta))

    print("Se crearon las carpetas")

    # Creamos una lista con los archivos y carpetas de la carpeta
    directorios = os.listdir(ruta)

    # Recorremos la lista de documentos
    for directorio in directorios:

        # Guardamos en una variable la ruta completa del archivo actual 
        ruta_archivo_actual = os.path.join(ruta, directorio)

        # Validación que sean archivos 
        if os.path.isfile(ruta_archivo_actual):

            # Guardamos la extensión del archivo en una variable
            formato_actual = os.path.splitext(ruta_archivo_actual)[1].lower()

            # Se hace una clasificación de los archivos y se mueven a su correspondiente carpeta
            if formato_actual in formatos_documento:
                shutil.move(ruta_archivo_actual, os.path.join(ruta_nueva, "Documentos"))
                print(f"Se movio el archivo {directorio}")
            elif formato_actual in formatos_video:
                shutil.move(ruta_archivo_actual, os.path.join(ruta_nueva, "Video"))
                print(f"Se movio el archivo {directorio}")
            elif formato_actual in formatos_imagen:
                shutil.move(ruta_archivo_actual, os.path.join(ruta_nueva, "Imagen"))
                print(f"Se movio el archivo {directorio}")
            elif formato_actual in formatos_audio:
                shutil.move(ruta_archivo_actual, os.path.join(ruta_nueva, "Audio"))
                print(f"Se movio el archivo {directorio}")
            else:
                shutil.move(ruta_archivo_actual, os.path.join(ruta_nueva, "Otros"))
                print(f"Se movio el archivo {directorio}")

    print("Finalizo el proceso")
         # print(os.path.splitext(ruta_archivo_actual)[1])

    #print(set(formatos))

