from logging import exception
import pandas as pd
import transform as tf
import load as ld
from logs import log
from sqlalchemy import create_engine
import psycopg2



if __name__ == '__main__':

    listas_df = tf.transform()
    
    ld.load(listas_df)

    # listas = ['venta', 'cliente', 'descripcion', 'tipo_producto', 'localidad', 'sede', 'empleados']

    # engine = create_engine(f'postgresql+psycopg2://postgres:sistema@localhost/auto_motors')
    # con = engine.connect()

    # listas_df.to_sql(venta, con=engine, index=False, if_exists='append')

    # with open('./sql/schema.sql', 'r') as myfile:
    #     data = myfile.read()
    #     engine.execute(data)



