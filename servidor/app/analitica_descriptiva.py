import datetime
import pandas as pd
import numpy as np
import csv

def leer_datos(file_name):
    datos_pandas = pd.read_csv(file_name, index_col=0, parse_dates=True)
    return datos_pandas

def guardar(data, file_name):    
    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(data)
        
def funcion_Maximo(datos, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]
    
    maximo = valores_temperatura.max()
    
    dato_guardar = [1, date_string, "Maximo", maximo]
    guardar(dato_guardar, file_name)
    return maximo

def funcion_Minimo(datos, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]
    
    minimo = valores_temperatura.min()
    
    dato_guardar = [2, date_string, "Minimo", minimo]
    guardar(dato_guardar, file_name)
    return minimo

def funcion_Mediana(datos, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]
    
    mediana = valores_temperatura.median()
    
    dato_guardar = [3, date_string, "Mediana", mediana]
    guardar(dato_guardar, file_name)
    return mediana

def funcion_Promedio(datos, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]
    
    promedio = valores_temperatura.mean()
    
    dato_guardar = [4, date_string, "Promedio", promedio]
    guardar(dato_guardar, file_name)
    return promedio

def funcion_Desviacion(datos, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]
    
    desviacion = valores_temperatura.std()
    
    dato_guardar = [5, date_string, "Desviacion", desviacion]
    guardar(dato_guardar, file_name)
    return desviacion

def funcion_Varianza(datos, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]
    
    varianza = valores_temperatura.var()
    
    dato_guardar = [6, date_string, "Varianza", varianza]
    guardar(dato_guardar, file_name)
    return varianza

def update(file_name):
    datos_pandas = leer_datos(file_name)
    funcion_Maximo(datos_pandas, file_name)
    funcion_Minimo(datos_pandas, file_name)
    funcion_Mediana(datos_pandas, file_name)
    funcion_Promedio(datos_pandas, file_name)
    funcion_Desviacion(datos_pandas, file_name)
    funcion_Varianza(datos_pandas, file_name)
    
    datos_graficar = leer_datos(file_name)
    return datos_graficar