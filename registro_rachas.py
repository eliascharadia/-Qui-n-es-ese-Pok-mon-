mejor_tiempo = 0
mejor_racha = 0
tiempo_promedio = '0 %'

import re

lista_rachas = []
with open("registro rachas.csv", "r") as archivo:
    for linea in archivo:
        registro = re.split(";|\n", linea)
        rachas = {}
        rachas["titulo"] = registro[0]
        rachas["valor"] = registro[1]
        lista_rachas.append(rachas)


print(lista_rachas)


with open("registro rachas.csv", "w") as archivo:

    for dato in lista_rachas:
        titulo_streak = dato["titulo"]

        match titulo_streak:
            case 'mejor tiempo':
                lista_rachas[0]["valor"] = mejor_tiempo
            case 'mejor racha':
                lista_rachas[1]["valor"] = mejor_racha
            case 'tiempo promedio':
                lista_rachas[2]["valor"] = tiempo_promedio
            case other:
                pass

    
    mensaje = f'{lista_rachas[0]["titulo"]};{lista_rachas[0]["valor"]}\n{lista_rachas[1]["titulo"]};{lista_rachas[1]["valor"]}\n{lista_rachas[2]["titulo"]};{lista_rachas[2]["valor"]}'

    archivo.write(mensaje)

print(lista_rachas)
