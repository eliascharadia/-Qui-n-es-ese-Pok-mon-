import json
import random

# with open("Pokemones 2 gen.json") as archivo:
#     datos = json.load(archivo)

# lista_pokemones = datos["pokemones"]
# print(len(lista_pokemones))
###### Elegir un pokemon random #########

def elegir_pokemon_random(lista1:list, lista2:list):
    """De la lista de pokemones selecciona un pokemon con todos sus datos de forma aleatoria 
    para poder trabajar con sus datos

    Args:
        personajes (list): contiene todos los datos necesarios de los pokemones.

    Returns:
        _type_: retorna un un diccionario con los datos del personaje.
    """
    listas_totales = [lista1,lista2]
    lista_random = random.choice(listas_totales)
    while lista_random == []:
        lista_random = random.choice(listas_totales)
    return random.choice(lista_random)

def devolver_ruta_imagen_cirueta_pokemon(datos_personajes:dict)-> str:
    """de los datos pasados se busca la ruta relativa de ls imagen cirueta del pokemon

    Args:
        datos_personajes (dict): diccionario con los datos de un pokemon

    Returns:
        str: retua relativa de la imagen cirueta
    """
    ruta_imagen = datos_personajes["cirueta"]
    return ruta_imagen

def devolver_ruta_imagen_revelada_pokemon(datos_personajes:dict)-> str:
    """de los datos pasados se busca la ruta relativa de ls imagen revelada del pokemon

    Args:
        datos_personajes (dict): diccionario con los datos de un pokemon

    Returns:
        str: retua relativa de la imagen revelada
    """
    ruta_imagen = datos_personajes["revelado"]
    return ruta_imagen

def obtener_ruta_imagen(datos_perosnajes:dict,key:str)->str:
    ruta_imagen = datos_perosnajes[key]
    return ruta_imagen

##############################################################################################

def borrar_de_lista_pokemon_ya_mostrado(diccionario_pokemon:str, lista_pokemones:list)->list:

    for i in range(len(lista_pokemones)):
        nombre_lista = lista_pokemones[i]["nombre_ingles"]
        nombre_diccionario = diccionario_pokemon["nombre_ingles"]
        if nombre_diccionario == nombre_lista:
            del lista_pokemones[i]
            break#Si no pongo este break, y elimino el elemento en la posición cero
        #no puede encontrar el elemento que estaba en la posicion 1 porque la lista ya fue modificada
        #y rompe el programa.


    return lista_pokemones

def devolver_lista_actualizada(diccionario:dict,lista_pokemones:list)->list:
    lista_actualizada = borrar_de_lista_pokemon_ya_mostrado(diccionario,lista_pokemones)
    return lista_actualizada

def verificar_existencia_pokemon_ingresado(lista_pokemones:list,nombre_ingresado:str):
    existencia = False
    for personaje in lista_pokemones:
        nombre = personaje["nombre_ingles"]
        if nombre == nombre_ingresado:
            existencia = True

    return existencia


def calcular_tiempo(tiempo_actual:float, tiempo_referencia, tiempo_duracion):
    temporizador_finalizado = False
    if tiempo_referencia != False:#En la primera vuelta es False asi que no entra en esta condicion.
            #cuando presiono enter cambio el valor de la cambiar_pokemon y entonces entra a esta condicion.
            if (tiempo_actual - tiempo_referencia) >= tiempo_duracion:#Hago la resta del tiempo al que esta corriendo menos el tiempo que 
                #se capturo cuando presione la telca enter. Si es mayor a 3 segundos 
                temporizador_finalizado = True
            
    
    return temporizador_finalizado

