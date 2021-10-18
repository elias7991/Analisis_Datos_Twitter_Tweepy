import os


"""*******************************PARAMETROS UTILIZADOS*******************************"""
# declaramos un diccionario vacio que contendra las palabras mas comunes
tendencias_all_tweets = {}
tendencias_tweets = {}
# palabras excluidas
palabras_excluidas = [
    'el', 'la', 'los', 'las', 'un', 'una', 'unos', 'unas', 'al', 'del', 'lo', 'le', 'y',
    'e', 'o', 'u', 'de', 'a', 'en', 'que', 'es', 'por', 'para', 'con', 'se', 'su', 'les',
    'me', 'q', 'te', 'pero', 'mi', 'ya', 'cuando', 'como', 'estoy', 'voy', 'porque', 'he',
    'son', 'solo', 'tengo', 'muy', 'no', 'ni', 'Yolanda', 'Park', 'yolanda', 'park', 'tu',
    'sus', 'si', 'park,', 'vos'
]


"""***************************RECUPERAR INFORMACION DEL FICHERO 1*******************************"""
try:
    # abrimos el fichero para leerlo
    fichero_all_tweets = open('conjunto_1_limpio.txt', 'r', encoding='utf-8')
    for linea in fichero_all_tweets:
        palabras = linea.strip().lower().split()
        for palabra in palabras:
            if (palabra not in palabras_excluidas) and len(palabra)>3:
                # busca la clave "palabra" y le agrega uno, si no hay lo pone en uno.
                tendencias_all_tweets[palabra] = tendencias_all_tweets.get(palabra, 0) + 1
finally:
    # cerramos nuestro fichero
    fichero_all_tweets.close()


"""*****************ESCRIBIMOS EN UN ARCHIVO EL DICCIONARIO DE RESULTADOS****************"""
lista_tendencias_1 = open('lista_tendencias_1.txt', 'w', encoding='utf-8')
# con esto ordenamos el diccionario por valor
todas_mas_usadas = sorted(tendencias_all_tweets, key=tendencias_all_tweets.get, reverse=True)
# ahora necesitamos escribir los valores ordenados pero con los valores correspondientes
for palabra in todas_mas_usadas:
    lista_tendencias_1.write(palabra + ":" + str(tendencias_all_tweets[palabra]) + "\n")

lista_tendencias_1.close()


"""***************************RECUPERAR INFORMACION DEL FICHERO 2*******************************"""
try:
    # abrimos el fichero para leerlo
    fichero_tweets = open('conjunto_2_limpio.txt', 'r', encoding='utf-8')
    for linea in fichero_tweets:
        palabras = linea.strip().lower().split()
        for palabra in palabras:
            if (palabra not in palabras_excluidas) and (len(palabra)>3):
                tendencias_tweets[palabra] = tendencias_tweets.get(palabra, 0) + 1
finally:
    fichero_tweets.close()


"""*****************ESCRIBIMOS EN UN ARCHIVO EL DICCIONARIO DE RESULTADOS****************"""
lista_tendencias_2 = open('lista_tendencias_2.txt', 'w', encoding='utf-8')
# con esto ordenamos el diccionario por valor
mas_usadas = sorted(tendencias_tweets, key=tendencias_tweets.get, reverse=True)
# ahora necesitamos escribir los valores ordenados pero con los valores correspondientes
for palabra in mas_usadas:
    lista_tendencias_2.write(palabra + ":" + str(tendencias_tweets[palabra]) + "\n")

lista_tendencias_2.close()


"""******************************INTERSECCION Y DIFERENCIA******************************"""
# retornamos todas las claves del diccionario que contiene todos los tweets en un rango de fechas
claves_1 = tendencias_all_tweets.keys()
# retornamos todas las claves del diccionario que contiene todos los tweets filtrados por un query
claves_2 = tendencias_tweets.keys()
# lista que contendra todas las palabras que esten dentro del conjunto interseccion
interseccion = []
# lista que contendra la diferencia Conjunto 1 - Conjunto 2
uno_no_dos = []
# lista que contendra la diferencia Conjunto 2 - Conjunto 1
dos_no_uno = []
interseccion_y = []
uno_no_dos_y = []
dos_no_uno_y = []

for palabra in claves_1:
    if palabra in claves_2:
        # como esta contenida en claves_1 y claves_2 forma parte de la interseccion
        interseccion.append(palabra)
        # numero de veces que se repite en 1 + numero de veces en 2
        interseccion_y.append(tendencias_all_tweets[palabra] + tendencias_tweets[palabra])
    else:
        #contenido en 1 pero no en 2
        uno_no_dos.append(palabra)
        uno_no_dos_y.append(tendencias_all_tweets[palabra])

for palabra in claves_2:
    if palabra not in claves_1:
        # palabra del conjunto 2 que no pertenece al conjunto 1
        dos_no_uno.append(palabra)
        dos_no_uno_y.append(tendencias_tweets[palabra])

"""*****************************BUSCAR LEN()>2*****************************"""
fichero_3 = open('conjunto_3.txt', 'w', encoding='utf-8')

for palabra in interseccion:
    if len(palabra) > 2:
        fichero_3.write(palabra + '\n')

fichero_3.close()


"""************************MOSTRAR DIFERENCIAS*****************************"""
fichero_8_1 = open('conjunto_8_1.txt', 'w', encoding='utf-8')
for palabra in uno_no_dos:
    fichero_8_1.write(palabra + os.linesep)

fichero_8_2 = open('conjunto_8_2.txt', 'w', encoding='utf8')
for palabra in dos_no_uno:
    fichero_8_2.write(palabra + os.linesep)


"""***********************************UNION***********************************"""
# lista que contendra todas las palabras que esten dentro del conjunto union
union = interseccion + uno_no_dos + dos_no_uno
union_y = interseccion_y + uno_no_dos_y + dos_no_uno_y

"""*****************************BUSCAR LEN()>2*****************************"""
fichero_4 = open('conjunto_4.txt', 'w', encoding='utf-8')

for palabra in union:
    if len(palabra) > 2:
        fichero_4.write(palabra + os.linesep)

fichero_4.close()
