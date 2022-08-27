import pandas as pd
from logs import log

def load(df):
    
    # tabla de hechos venta
    log('Convirtiendo DataFrame ventas a csv')
    df[0].to_csv('./out/venta.csv', index=False)


    # Tabla dimenciones cliente
    log('Convirtiendo DataFrame ventas a csv')
    df[1].to_csv('./out/cliente.csv', index=False)


    # Tabla dimenciones descripcion
    log('Convirtiendo DataFrame descripcion a csv')
    df[2].to_csv('./out/descripcion.csv', index=False)


    # Tabla dimenciones tipo_producto
    log('Convirtiendo DataFrame tipo_producto a csv')
    df[3].to_csv('./out/tipo_producto.csv', index=False)


    # Tabla dimenciones localidad
    log('Convirtiendo DataFrame localidad a csv')
    df[4].to_csv('./out/localidad.csv', index=False)


    # Tabla dimenciones sede
    log('Convirtiendo DataFrame sede a csv')
    df[5].to_csv('./out/sede.csv', index=False)


    # Tabla dimenciones empleados
    log('Convirtiendo DataFrame empleados a csv')
    df[6].to_csv('./out/empleados.csv', index=False)
    
    return df
