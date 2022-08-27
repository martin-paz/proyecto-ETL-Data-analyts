# %%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from logs import log

#funcion para calcular outliers
def outliers_obt(data, columna,cuartial1,cuartil2,valoriqr=1.5):
    ##calculamos los cuartiles 
    Q1 = data[columna].quantile(float(cuartial1))
    #print('Primer Cuartile', Q1)
    Q3 = data[columna].quantile(float(cuartil2))
    #print('Tercer Cuartile',Q3)
    IQR = Q3 - Q1
    #print('Rango intercuartile', IQR)

    ##calculamos los bigotes superior e inferior
    BI = (Q1 - valoriqr * IQR)
    #print('bigote Inferior \n', BI)
    BS = (Q3 + valoriqr * IQR)
    #print('bigote superior \n', BS)

    ##obtenemos una nueva tabla sin los outliers
    ubi_sin_out = data[(data[columna] >= BI) & (data[columna] <= BS)]
    return ubi_sin_out



def transform():
    
    log('Levantando los Dataset')
    venta = pd.read_csv('./dataset/ventas.csv', delimiter=';', dtype='unicode')
    empleados = pd.read_csv('./dataset/Empleados.csv', delimiter=';')

    log('FIN - carga de los csv')

    
    log('INICIO - Comienzan las TRANSFORMACIONES')
    venta.dropna(inplace=True)

    venta.drop(venta[venta['Ventas'] >= '50.000.000.00'].index, inplace=True)


    venta.Cantidad = venta.Cantidad.str.replace(',','')
    venta.Ventas = venta.Ventas.str.replace(',','.')


    venta = venta.astype({  'Fecha':'datetime64[ns]'})
    venta = venta.astype({  'CodigoFamilia':'int64',
                            'Cantidad':'int64',
                            'Ventas':'float64',
                            'Area':'int64',
                            'Empleado':'int64'
                            })


    venta.rename(columns={'Empleado':'Id_Empleado','IdCliente':'Id_Cliente'}, inplace=True)

    venta = outliers_obt(venta,'Ventas','0.25','0.75', valoriqr=2)

    venta = outliers_obt(venta,'Cantidad','0.25','0.8499999', valoriqr=1.75)

    venta['Total_ventas_usd'] = venta.Ventas * venta.Cantidad * 0.00023

    venta.reset_index(inplace=True)
    venta.rename(columns={'index':'Id_venta'}, inplace=True)
    venta.drop(columns=['Id_venta'], inplace=True)
    venta.reset_index(inplace=True)
    venta.rename(columns={'index':'Id_venta'}, inplace=True)
    venta.Id_venta = venta.Id_venta.map(lambda x: x + 1)
    log('FIN - TRANSFORMACIONES')

    log('INICIO - CREACION TABLAS DE HECHOS')
    log('CLIENTE')
    cliente = venta[['Id_Cliente','NombreCliente']].drop_duplicates().copy()

    log('DESCRIPCION')
    descripcion = venta[['Descripcion']].drop_duplicates().copy()
    descripcion.reset_index(inplace=True)
    descripcion.rename(columns={'index':'Id_Descripcion'}, inplace=True)
    descripcion.Id_Descripcion=descripcion.Id_Descripcion.map(lambda x : (x + 1))

    log('TIPO DE PRODUCTO')
    tipo_producto = venta[['CodigoFamilia','Familia']].drop_duplicates().copy()
    tipo_producto.rename(columns={'CodigoFamilia':'Id_Tipoproducto','Familia':'Tipoprodcuto'}, inplace=True)
    tipo_producto.reset_index(inplace=True)
    tipo_producto.drop(columns=['index'], inplace=True)

    log('LOCALIDAD')
    localidad = venta[['Localidad']].drop_duplicates().copy()
    localidad.reset_index(inplace=True)
    localidad.rename(columns={'index':'Id_Localidad'}, inplace=True)
    localidad.drop(columns=['Id_Localidad'], inplace=True)
    localidad.reset_index(inplace=True)
    localidad.rename(columns={'index':'Id_Localidad'}, inplace=True)
    localidad.Id_Localidad = localidad.Id_Localidad.map(lambda x: x + 1)

    log('SEDE')
    sede = venta[['Sede','Area']].drop_duplicates().copy()
    sede.reset_index(inplace=True)
    sede.rename(columns={'index':'Id_Sede'},inplace=True)
    sede.drop(columns=['Id_Sede'], inplace=True)
    sede.reset_index(inplace=True)
    sede.rename(columns={'index':'Id_Sede'},inplace=True)
    sede.Id_Sede = sede.Id_Sede.map(lambda x: x + 1)
    log('FIN - Creacion Tablas Hechos')

    log('CREACION - TABLA HECHOS')
    log('VENTA')
    venta = pd.merge(venta,descripcion, left_on='Descripcion', right_on='Descripcion')
    venta.rename(columns={'CodigoFamilia':'Id_Tipoproducto', 'Familia':'Tipoprodcuto'}, inplace=True)
    venta= pd.merge(venta, localidad, left_on='Localidad', right_on='Localidad')
    venta = pd.merge(venta, sede, left_on='Area', right_on='Area')
    venta.drop(columns=['NombreCliente','Descripcion','Tipoprodcuto','Localidad','Sede_x','Area','Sede_y'], inplace=True)
    venta = venta[['Id_venta','Fecha','Id_Cliente','Id_Empleado','Id_Tipoproducto','Id_Descripcion','Id_Localidad','Id_Sede','Cantidad','Ventas','Total_ventas_usd']]

    lista_tablas = [venta, cliente, descripcion, tipo_producto, localidad, sede, empleados]

    return lista_tablas


