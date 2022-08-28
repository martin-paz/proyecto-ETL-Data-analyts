import pandas as pd
from logs import log
from sqlalchemy import create_engine

def load(df):
    
    # tabla de hechos venta
    log('Convirtiendo DataFrame ventas a csv')
    df[0].to_csv('C:/Users/Public/data/auto_motors/venta.csv', index=False)
    engine = create_engine(f'postgresql+psycopg2://postgres:sistema@localhost/auto_motors')
    df[0].to_sql('venta', con=engine, index=False, if_exists='append')


    # Tabla dimenciones cliente
    log('Convirtiendo DataFrame ventas a csv')
    df[1].to_csv('C:/Users/Public/data/auto_motors/cliente.csv', index=False)
    engine = create_engine(f'postgresql+psycopg2://postgres:sistema@localhost/auto_motors')
    df[1].to_sql('cliente', con=engine, index=False, if_exists='append')


    # Tabla dimenciones descripcion
    log('Convirtiendo DataFrame descripcion a csv')
    df[2].to_csv('C:/Users/Public/data/auto_motors/descripcion.csv', index=False)
    engine = create_engine(f'postgresql+psycopg2://postgres:sistema@localhost/auto_motors')
    df[2].to_sql('descripcion', con=engine, index=False, if_exists='append')


    # Tabla dimenciones tipo_producto
    log('Convirtiendo DataFrame tipo_producto a csv')
    df[3].to_csv('C:/Users/Public/data/auto_motors/tipo_producto.csv', index=False)
    engine = create_engine(f'postgresql+psycopg2://postgres:sistema@localhost/auto_motors')
    df[3].to_sql('tipo_producto', con=engine, index=False, if_exists='append')


    # Tabla dimenciones localidad
    log('Convirtiendo DataFrame localidad a csv')
    df[4].to_csv('C:/Users/Public/data/auto_motors/localidad.csv', index=False)
    engine = create_engine(f'postgresql+psycopg2://postgres:sistema@localhost/auto_motors')
    df[4].to_sql('localidad', con=engine, index=False, if_exists='append')


    # Tabla dimenciones sede
    log('Convirtiendo DataFrame sede a csv')
    df[5].to_csv('C:/Users/Public/data/auto_motors/sede.csv', index=False)
    engine = create_engine(f'postgresql+psycopg2://postgres:sistema@localhost/auto_motors')
    df[5].to_sql('sede', con=engine, index=False, if_exists='append')


    # Tabla dimenciones empleados
    log('Convirtiendo DataFrame empleados a csv')
    df[6].to_csv('C:/Users/Public/data/auto_motors/empleados.csv', index=False)
    engine = create_engine(f'postgresql+psycopg2://postgres:sistema@localhost/auto_motors')
    df[6].to_sql('empleados', con=engine, index=False, if_exists='append')
    

    with open('./sql/schema.sql', 'r') as myfile:
        data = myfile.read()
        engine.execute(data)


    return df
