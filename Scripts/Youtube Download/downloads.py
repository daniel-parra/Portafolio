from pytube import YouTube
from argparse import ArgumentParser

def pasar_argumentos():
    parser = ArgumentParser()
    parser.add_argument( "--url", 
                         "-u", 
                         dest="url", 
                         type=str, 
                         help="""Define la url del recurso a descargar. 
                         Se debe enviar la ruta encerrada entre comillas dobles""",
                         required=True)
    parser.add_argument("--audio",
                        "-a",
                        dest="audio",
                        action="store_true",
                        help="""Define el formato con el que se descarga el recurso""",
                        default=False)
    parser.add_argument("--formato",
                        "-f",
                        dest="formato",
                        type=str,
                        help="""Define el formato con el que se descarga el recurso""")

    return parser.parse_args()

def descargar(recurso):
    print(f"Descargando \"{recurso.title}\" ...")
    recurso.download()
    print("Descarga completada")

arg = pasar_argumentos()

if arg.url != None:
    url = arg
else: 
    url = input("Insertar dirección url:\n>")

yt = YouTube(url)

if arg.audio is True and arg.formato != None: 
    audio = yt.streams.filter(only_audio=True).first()
    descargar(audio)
if arg.audio is False and arg.formato != None:
    yt.streams.filter(progressive=True, file_extension=arg.formato).order_by('resolution').desc().first()
    descargar(yt)
else:
    yt.streams.first()
    descargar(yt)
