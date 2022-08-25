import pandas as pd
from sqlalchemy import create_engine
import psycopg2


try:
    conexion = psycopg2.connect(database='auto_motors', user='postgres', password='sistema')
    cursor01=conexion.cursor()
    cursor01.execute('select version()')
    version=cursor01.fetchone()
except Exception as err:
    print('Error al conectar a la base', err)
else:
    print(version)



conexion.close()