#exportamos las librerias necesarias para el analisis de nuestro Dataset
import pandas as pd #para trabajar con dataframes
import os #para trabajar con los archivos
import re #para trabajar con expresiones regulares

def ruta_carpeta_ETFs():
    path= '/Users/hectorbernaltrujillo/Downloads/archive (3)/ETFs'
    os.chdir(path)
ruta_carpeta_ETFs()

def union_datos_ETFs(path):
    archivos= [x for x in os.listdir() if re.search ('.txt', x)]
    df= pd.DataFrame()
    for i in archivos:
        archivo= pd.read_csv(i)
        df=pd.concat([df, archivo])
    df.to_csv('union_datos_ETFs.csv')
    return df
union_datos_ETFs(ruta_carpeta_ETFs())

