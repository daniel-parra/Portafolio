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
print(password) #danger13 - p\r^{kPfd0Nj,U$m
#https://accounts.palia.com/sign-up?referral=2efb6220-f559-45b8-8485-cfd63205e9fd


