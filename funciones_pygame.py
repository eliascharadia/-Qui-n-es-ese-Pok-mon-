import pygame
from Logica import *
import re

def transformar_imagen(ruta):
    imagen = pygame.image.load(ruta)
    imagen = pygame.transform.scale(imagen,(400,500))
    return imagen

def dibujar_rectangulo(pantalla, color,dimensiones):
    pygame.draw.rect(pantalla, color, dimensiones)

def renderizar_texto(fuente,texto, color):
    texto_renderizado = fuente.render(texto,False,color)
    return texto_renderizado

def renderizar_texto_variable(fuente,texto_variable, color):
    texto_renderizado = fuente.render(f'{texto_variable:0.2f}',False,color)
    return texto_renderizado

def subir_texto_pantalla(pantalla,texto,posicion, fuente, color):

    if type(texto) == float or type(texto) == int:
        texto_renderizado = renderizar_texto(fuente, f'{texto:0.2f}', color)
        pantalla.blit(texto_renderizado,posicion)
    else:
        texto_renderizado = renderizar_texto(fuente,texto, color)
        pantalla.blit(texto_renderizado,posicion)
        

def leer_archivo_streaks(path:str):
    lista_datos = []
    with open(path, "r") as archivo:
        for linea in archivo:
            registro = re.split(";|\n", linea)
            datos = {}
            datos["titulo"] = registro[0]
            datos["valor"] = registro[1]
            lista_datos.append(datos)

    return lista_datos

def obtener_datos_archivo(path, clave):
    lista_datos = leer_archivo_streaks(path)
    
    for diccionario in lista_datos:
        if diccionario['titulo'] == clave:
            dato_requerido = diccionario['valor']
            dato_requerido = float(dato_requerido)
            break
    
    return dato_requerido

