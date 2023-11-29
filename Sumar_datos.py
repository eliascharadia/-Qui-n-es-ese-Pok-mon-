import json
# nuevo_dato = {
#     "nombre_ingles":"starmie",
#     "nombre_frances":"stari",
#     "nombre_aleman":"starmie",
#     "nombre_japones":"sutami",
#     "nombre_chino":"baoshi haixing",
#     "cirueta":"Imagenes_ciruetas\Starmie.PNG",
#     "revelado":"Imagenes_reveladas_completas\Starmie.PNG"
#     }



# with open("Pokemones.json") as archivo:
#     data = json.load(archivo)#leo el archivo

# archivo_modificado = data["pokemones"].append(nuevo_dato)

# with open("Pokemones.json", "w") as archivo:
#     json.dump(data, archivo,indent=4)#escribe el archivo



nuevo_dato = {
    "nombre_ingles":"xatu",
    "nombre_frances":"xatu",
    "nombre_aleman":"xatu",
    "nombre_japones":"neitio",
    "nombre_chino":"tian goushen",
    "cirueta":"Imagenes ciruetas 2 gen\\xatu.PNG",
    "revelado":"Imganes reveladas 2 gen\\xatu.PNG"
    }

# data = {"pokemones":[]}
# with open("Pokemones 2 gen.json", "w") as archivo:
#     json.dump(data, archivo,indent=4)#escribe el archivo

with open("Pokemones 2 gen.json") as archivo:
    data = json.load(archivo)#leo el archivo

archivo_modificado = data["pokemones"].append(nuevo_dato)

with open("Pokemones 2 gen.json", "w") as archivo:
    json.dump(data, archivo,indent=4)#escribe el archivo