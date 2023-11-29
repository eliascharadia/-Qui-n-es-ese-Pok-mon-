from Colores import *
from Logica import *
from funciones_pygame import *
import pygame
import re


pygame.init()

screen = pygame.display.set_mode((800,800))
#Fuentes
base_font = pygame.font.SysFont("Arial", 20)
fuentes_titulos = pygame.font.SysFont("Elephant",15)
fuentes_titulo_datos_finales = pygame.font.SysFont("Elephant",20)
fuente_nombres = pygame.font.SysFont("Negrita", 30)
fuente_datos_strakes = pygame.font.SysFont("Negrita",22)
#Rectangulos
input_rect = pygame.Rect(300,700,140,32)
#Color
color = (226, 234, 243)
color_btn_gen1 = AZUL_CELESTE_OBSCURO
color_btn_gen2 = AZUL_CELESTE_OBSCURO


clock = pygame.time.Clock()
pygame.display.set_caption("Adivina el pokemon")


with open("Pokemones 1 gen.json") as archivo:
    datos_gen1 = json.load(archivo)

with open("Pokemones 2 gen.json") as archivo:
    datos_gen2 = json.load(archivo)


## LECTURA DE STREAKS GUARDADOS
tiempo_racha = obtener_datos_archivo("registro rachas.csv", "mejor tiempo")
mejor_racha = obtener_datos_archivo("registro rachas.csv", "mejor racha")
promedio = obtener_datos_archivo("registro rachas.csv", "tiempo promedio")
contador_rachas_superadas = obtener_datos_archivo("registro rachas.csv", "rachas superadas")
tiempo_racha_total = obtener_datos_archivo("registro rachas.csv", "suma de tiempos")

# Texto en caja de texto inicial
user_text = ""
tiempo_pregunta_pokemon = "-"

#Banderas booleanas
cambiar_pokemon = True
flag = True
tiempo_cuando_presiono_enter = False
tiempo_saltar_pokemon = False
presiono_btn_gen1 = True
presiono_btn_gen2 = False
# Variables inicializadas en cero
racha = 0
contador_de_jugadas = 0
racha_actual = 0




#Inicio del blucle
while flag:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag = False
        elif evento.type == pygame.KEYDOWN:#Pregunta por eventos causados al presionar cualquier tecla
            if evento.key == pygame.K_RETURN:#Pregunto si la letra que se presiono es el enter

                tiempo_cuando_presiono_enter = pygame.time.get_ticks()/1000#Tiempo capturado al presionar la tecla enter

                texto_ingresado = user_text
                texto_ingresado = texto_ingresado.lower()
                user_text = ""
                
                ###### aumento racha #####
                nombre_pokemon_jugando = pokemon_random["nombre_ingles"]#Capturo o guardo el nombre del pokemon actual.

                if nombre_pokemon_jugando == texto_ingresado:#Pregunto si el nombre ingresado es igual al nombre del pokemon de la cirueta
                    racha_actual += 1
                    contador_rachas_superadas += 1
                    if mejor_racha == 0 or racha_actual > mejor_racha:
                        mejor_racha = racha_actual
                    
                    
                    ######## calculo del mejor tiempo (tiempo racha )#########
                    tiempo_pregunta_pokemon = tiempo_cuando_presiono_enter - tiempo_cuando_cambia_pokemon# Con esto guardo el tiempo de la pregunta anterior
                    tiempo_racha_total += tiempo_pregunta_pokemon
                    promedio = tiempo_racha_total / contador_rachas_superadas

                    if tiempo_racha == 0 or tiempo_pregunta_pokemon < tiempo_racha:    
                        tiempo_racha = tiempo_pregunta_pokemon 
                else:    
                    racha_actual = 0
                    contador_de_jugadas = 11
                    

            elif evento.key == pygame.K_BACKSPACE:#Si se presiono la tecla de borrar borro un caracter
                user_text = user_text[:-1]
            
            else:
                user_text += evento.unicode # Sumo la letra que se presiono, en la caja de texto.

        elif evento.type == pygame.MOUSEBUTTONDOWN:
                pos_x = evento.pos[0]
                pos_y = evento.pos[1]
                # print((pos_x,pos_y))
                if pos_x >= 25 and pos_x <= (25+150) and pos_y >= 100 and pos_y <= (100+60):
                    if presiono_btn_gen1 and presiono_btn_gen2:
                        presiono_btn_gen1 = False
                    else:
                        presiono_btn_gen1 = True 

                elif pos_x >= 25 and pos_x <= (25+150) and pos_y >= 200 and pos_y <= (200+60):
                    if presiono_btn_gen2 and presiono_btn_gen1:
                        presiono_btn_gen2 = False
                    else:
                        presiono_btn_gen2 = True   

                elif pos_x >= 500 and pos_x <= (500+75) and pos_y >= 600 and pos_y <= (600+ 30): 
                    # Esta logica pregunta si donde se presiono dentro de la pantalla esta unicado
                    # el boton de saltar pokemon.
                    tiempo_saltar_pokemon = pygame.time.get_ticks()/1000 # tomo el tiempo cuando apreta el bton de cambiar pokemon
                    texto_ingresado = "No sabe el nombre"


    screen.fill("grey")
    
    if contador_de_jugadas < 10:

        ### BOTONES DE GENERACIONES ###
        dibujar_rectangulo(screen,color_btn_gen1,(25,100,150,60))
        

        dibujar_rectangulo(screen,color_btn_gen2,(25,200,150,60))
        
        if presiono_btn_gen1:
            color_btn_gen1 = BORDO
            subir_texto_pantalla(screen,"GEN 1 ☑",(70,120),fuentes_titulos, "white")
            lista_pokemones_g1 = datos_gen1["pokemones"]
        else:
            color_btn_gen1 = AZUL_CELESTE_OBSCURO
            subir_texto_pantalla(screen,"GEN 1",(70,120),fuentes_titulos, "white")
            lista_pokemones_g1 = []

        if presiono_btn_gen2:
            color_btn_gen2 = BORDO
            subir_texto_pantalla(screen,"GEN 2 ☑",(70,220),fuentes_titulos, "white")
            lista_pokemones_g2 = datos_gen2["pokemones"]
        else:
            color_btn_gen2 = AZUL_CELESTE_OBSCURO
            subir_texto_pantalla(screen,"GEN 2",(70,220),fuentes_titulos, "white")
            lista_pokemones_g2 = [] 




        ############# ELIJO UN POKEMON RANDOM #############
        if cambiar_pokemon == True:
            pokemon_random = elegir_pokemon_random(lista_pokemones_g1, lista_pokemones_g2)
            texto_ingresado = ""
            cambiar_pokemon = False
            tiempo_cuando_cambia_pokemon = pygame.time.get_ticks()/1000# Tomo el tiempo del pokemon actual
            

          
        ################# GENERO LAS RUTAS DE LA IMAGENES #########################
        if texto_ingresado == "":
            ruta = obtener_ruta_imagen(pokemon_random,"cirueta")
            #### Limpio la seccion de mostrado de los nombres
            
            #muestro caja de texto vacia
            pygame.draw.rect(screen,color,(input_rect))
            text_surface = base_font.render(user_text,False,(0,0,0))
            screen.blit(text_surface,(input_rect.x + 10,input_rect.y + 5))
        else:
            ruta = obtener_ruta_imagen(pokemon_random,"revelado")
            #### revelo el nombre en distintos idiomas ##########
            nombre_ingles = pokemon_random["nombre_ingles"]
            nombre_frances = pokemon_random["nombre_frances"]
            nombre_aleman = pokemon_random["nombre_aleman"]
            nombre_japones = pokemon_random["nombre_japones"] 
            nombre_chino = pokemon_random["nombre_chino"]   

            texto_titulo_nombres = fuentes_titulos.render("Tambien conocido como:",False,BORDO)    
            screen.blit(texto_titulo_nombres,(300,600))    
            texto_nombres = fuente_nombres.render(f'Francia: {nombre_frances} | Aleman: {nombre_aleman} | Japones: {nombre_japones} | Chino: {nombre_chino}',False, BORDO)
            screen.blit(texto_nombres,(50,630))
            
            ## MUESTRO CAJA DE TEXTO CON EL NOMBRE ORIGINAL DEL PERSONAJE
            pygame.draw.rect(screen,color,(input_rect))
            text_surface = base_font.render(nombre_ingles.upper(),False,(0,0,0))
            screen.blit(text_surface,(input_rect.x + 10,input_rect.y + 5))

        
        ###### MUESTRO LA IMAGEN #################
        imagen = transformar_imagen(ruta)
        screen.blit(imagen, (175,100))


        ########### TEMPORIZADOR DE 3 SEGUNDOS ###############
        tiempo_actual  = pygame.time.get_ticks()/1000
        temporizador_acerto_pokemon = calcular_tiempo(tiempo_actual, tiempo_cuando_presiono_enter, 3) 
        if temporizador_acerto_pokemon:
                cambiar_pokemon = True
                tiempo_cuando_presiono_enter = False
                ############## actualizar lista ##############
                lista_pokemones_gen1 = devolver_lista_actualizada(pokemon_random,lista_pokemones_g1)
                lista_pokemones_gen2 = devolver_lista_actualizada(pokemon_random,lista_pokemones_g2) 
                #LLEVO LAS CUENTAS DE LAS PARTIDAD JUGADAS
                contador_de_jugadas += 1

        temporizador_salto_de_pokemon = calcular_tiempo(tiempo_actual, tiempo_saltar_pokemon, 3)
        if temporizador_salto_de_pokemon:
            cambiar_pokemon = True
            tiempo_saltar_pokemon = False
            lista_pokemones_g1 = devolver_lista_actualizada(pokemon_random,lista_pokemones_g1)
            lista_pokemones_g2 = devolver_lista_actualizada(pokemon_random,lista_pokemones_g2)
            contador_de_jugadas += 1
        
                
                
                
        
        ######### INDICADORES DEL TIEMPO (TIEMPO RACHA) ###############
        dibujar_rectangulo(screen,AZUL_CELESTE_OBSCURO,(575,300,150,60))
        subir_texto_pantalla(screen,'RACHA TIEMPO: ',(575,305),fuentes_titulos, "white")
        subir_texto_pantalla(screen,tiempo_racha,(630,330), fuente_datos_strakes, "white")

        ######### TIEMPO DE LA PREGUNTA ANTERIOR ##########
        dibujar_rectangulo(screen, AZUL_CELESTE_OBSCURO,(575,400,200,60))
        subir_texto_pantalla(screen,"Tiempo Pregunta anterior: ", (575,405), fuentes_titulos, "white")
        subir_texto_pantalla(screen,tiempo_pregunta_pokemon, (650,435), fuente_datos_strakes, "white")

        #### INDICADORES DE RACHAS ######
        dibujar_rectangulo(screen, AZUL_CELESTE_OBSCURO,(575,100,150,60))
        subir_texto_pantalla(screen,"Racha actual: ", (600,100), fuentes_titulos, "white")
        subir_texto_pantalla(screen,racha_actual, (630,125), fuente_datos_strakes, "white")

        dibujar_rectangulo(screen, AZUL_CELESTE_OBSCURO,(575,170,150,60))
        subir_texto_pantalla(screen,"Mejor racha: ", (600,170), fuentes_titulos, "white")
        subir_texto_pantalla(screen,mejor_racha, (630,195), fuente_datos_strakes, "white")


        ### promedio de los tiempos superados ###
        dibujar_rectangulo(screen, AZUL_CELESTE_OBSCURO,(575,470,150,60))
        subir_texto_pantalla(screen,"Promedio:", (600,475), fuentes_titulos, "white")
        subir_texto_pantalla(screen,promedio, (630,500), fuente_datos_strakes, "white")
        



        ## Boton para pasar de pokemon ##
        dibujar_rectangulo(screen, AZUL_CELESTE_OBSCURO,(500,600,75,30))
        subir_texto_pantalla(screen,"Saltar", (510,608), fuente_datos_strakes, "white")

        

        


    elif contador_de_jugadas == 10:
               
        lista_rachas = leer_archivo_streaks("registro rachas.csv")
        ## ACTUALIZACION DE STREAKS GUARDADOS
        for i in range(len(lista_rachas)):
            titulo_streak = lista_rachas[i]['titulo']
            match titulo_streak:
                case 'mejor tiempo':
                    lista_rachas[i]["valor"] = tiempo_racha
                case 'mejor racha':
                    lista_rachas[i]["valor"] = mejor_racha
                case 'tiempo promedio':
                    lista_rachas[i]["valor"] = promedio
                case 'rachas superadas':
                    lista_rachas[i]["valor"] = contador_rachas_superadas
                case 'suma de tiempos':
                    lista_rachas[i]['valor'] = tiempo_racha_total
        

        with open("registro rachas.csv", "w") as archivo:
            mensaje = f'{lista_rachas[0]["titulo"]};{lista_rachas[0]["valor"]}\n{lista_rachas[1]["titulo"]};{lista_rachas[1]["valor"]}\n{lista_rachas[2]["titulo"]};{lista_rachas[2]["valor"]}\n{lista_rachas[3]["titulo"]};{lista_rachas[3]["valor"]}\n{lista_rachas[4]["titulo"]};{lista_rachas[4]["valor"]}'
            archivo.write(mensaje)


        nombre_ingles = pokemon_random["nombre_ingles"]
        subir_texto_pantalla(screen, f'- Se equivocó con el pokemon: {nombre_ingles}',(140,220), fuente_datos_strakes, AZUL_CELESTE_OBSCURO)
        racha = 0
        contador_de_jugadas += 1
    else:

        texto_game_over = fuentes_titulo_datos_finales.render("JUEGO FINALIZADO",False,AZUL_CELESTE_OBSCURO)
        screen.blit(texto_game_over,(260,50))
        sub_titulo = fuentes_titulos.render('Datos de la partida',False,AZUL_CELESTE_OBSCURO)
        screen.blit(sub_titulo,(130,130))

        racha_obtenida = fuente_datos_strakes.render(f'- Obtuvo una racha de: {racha_actual}',False,AZUL_CELESTE_OBSCURO)
        screen.blit(racha_obtenida,(140,160))

        su_mejor_racha = fuente_datos_strakes.render(f'- Su mejor racha registrada fue: {mejor_racha}',False,AZUL_CELESTE_OBSCURO)
        screen.blit(su_mejor_racha,(140,180))
        
        subir_texto_pantalla(screen,'- Mejor tiempo obtenido: ',(140, 200),fuente_datos_strakes, AZUL_CELESTE_OBSCURO)
        subir_texto_pantalla(screen,tiempo_racha,(320,200), fuente_datos_strakes, AZUL_CELESTE_OBSCURO)

       
            
        
                
    
    
    clock.tick(30)
    pygame.display.flip()
    pygame.display.update()

pygame.quit()
