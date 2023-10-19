import os
from os import path
import pathlib
import secrets
import string

def crear_password(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for _ in range(longitud):
        password += secrets.choice(caracteres)
    return password

password = crear_password(16)
print(password)


