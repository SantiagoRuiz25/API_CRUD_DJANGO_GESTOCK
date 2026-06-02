import os
from decouple import config

#leer el puerto .env
PORT = config('API_PORTT', cast=int)

#ejecutar el servidor django
os.system(f'python manage.py runserver {PORT}')