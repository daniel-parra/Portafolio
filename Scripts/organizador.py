import os
from datetime import date

if __name__ == '__main__':
    os.system('cls')
    ruta = r'C:\Users\DANIE\Downloads'

    formatos_documento = [".pdf", ".txt", '.pptx', '.docx', '.xls', '.epub']
    formatos_video = ['.mp4', '.avi']
    formatos_imagen = ['.jpeg', '.svg', '.png', '.jpg']
    formatos_audio = ['.mp3']
    
    fecha_actual = f"{date.today().year}{date.today().month}{date.today().day}"
    ruta_nueva = os.path.join(ruta, fecha_actual)

    if not os.path.isdir(ruta_nueva):
        os.mkdir(ruta_nueva)

    if not os.path.isdir(os.path.join(ruta_nueva, "Documentos")):
        os.mkdir(os.path.join(ruta_nueva, "Documentos"))

    if not os.path.isdir(os.path.join(ruta_nueva, "Video")):
        os.mkdir(os.path.join(ruta_nueva, "Video"))
    
    if not os.path.isdir(os.path.join(ruta_nueva, "Audio")):
        os.mkdir(os.path.join(ruta_nueva, "Audio"))
    
    if not os.path.isdir(os.path.join(ruta_nueva, "Imagen")):
        os.mkdir(os.path.join(ruta_nueva, "Imagen"))

    if not os.path.isdir(os.path.join(ruta_nueva, "Otros")):
        os.mkdir(os.path.join(ruta_nueva, "Otros"))

    directorios = os.listdir(ruta)

    formatos = []

    for directorio in directorios:
        ruta_archivo_actual = os.path.join(ruta, directorio)
        if os.path.isfile(ruta_archivo_actual):
            formatos.append(os.path.splitext(ruta_archivo_actual)[1])
         # print(os.path.splitext(ruta_archivo_actual)[1])

    #print(set(formatos))

