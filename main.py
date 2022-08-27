from logging import exception
import pandas as pd
import sys
import transform as tf
import load as ld
from logs import log
from sqlalchemy import create_engine



if __name__ == '__main__':

    listas_df = tf.transform()
    
    ld.load(listas_df)

    engine = create_engine(f'postgresql://postgres:sistema@localhost:5432/auto_motors')
    con = engine.connect()
    #cursor = con.execute()
    try:
        with open('./sql/schema.sql', 'r') as myfile:
            data = myfile.read()
            engine.execute(data)
    except ValueError as vx:
        print(vx)
    except exception as ex:
        print(ex)
    else:
        print('Datos %s fueron insterados en el data werehouse.' %data)


