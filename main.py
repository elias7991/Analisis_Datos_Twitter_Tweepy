# libreria de python que facilita el uso de la API de twitter
import tweepy as tw
# libreria que se utilizara para recuperar la fecha actual
from datetime import datetime
# libreria que se utiliza para dar el salto de linea al escribir en el archivo
import os
# libreria de emojis
import emoji
import pandas
import matplotlib.pyplot as plot

"""
**********************************************************************************************************
************************************AUTENTICACION CON PROTOCOLO OAuth2************************************
**********************************************************************************************************
"""

"""*************************************VARIABLES DE AUTENTICACION*************************************"""
consumer_key = "H2cC7eKrsCHqBoBZG6XYNeFAi"
consumer_secret = "z2d9Riqn3JyeOvkQ0R0E6P89Huo22SEB92GdwAbK69SsS4zt3i"
access_token = "1443289288817483787-Y23CyxwSuGhXX0M6yZzGKbmsvqNMQV"
access_token_secret = "18nVpC79FpzY46PrkAQiB9gbXCT7XTRvoL1bJQQbtXIDr"
"""************************************AUTENTICACION***************************************************"""
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
"""
    con el argumento True de wait_on_rate_limit podemos hacer que nuestro programa espere a tener
    cupo de descarga nuevamente y que no termine de ejecutarse.
"""
api = tw.API(auth, wait_on_rate_limit=True)


"""********************************PARÁMETROS DE BÚSQUEDA****************************"""
# definimos la palabra y/o frase que vamos a buscar o una lista para iterar despues
search_word = "Yolanda Park"
# trae la fecha de hoy en formato de cadena
today = datetime.today().strftime('%Y-%m-%d')
# asignamos la fecha de hoy para buscar los tweets más actuales siempre
date_until = today
# definimos el número máximo de tweets que vamos a buscar
max_tweets = 1000

"""
    **********************************************************************************
    ******************************RECUPERACION DE TWEETS******************************
    **********************************************************************************
"""

"""***********************************CONJUNTO 1 DE TWEETS****************************"""
"""***********************************SIN QUERY PARTICULAR****************************"""
all_tweets = tw.Cursor(
    api.search_tweets,
    q="*",
    lang="es",
    until=date_until,
    tweet_mode="extended"
).items(max_tweets)

"""***********************************CONJUNTO 2 DE TWEETS***************************"""
"""***********************************CON UNA QUERY**********************************"""
tweets = tw.Cursor(
    api.search_tweets,
    # q, de query
    q=search_word,
    lang="es",
    until=date_until,
    # para traer el tweet completo sin truncar en el caracter 140
    tweet_mode="extended"
).items(max_tweets)


"""*************************PREPARAR LOS FICHEROS A UTILIZAR***************************"""
fichero_all_tweets = open('conjunto_1.txt', 'w', encoding="utf-8")
fichero_tweets = open('conjunto_2.txt', 'w', encoding="utf-8")

# diccionario que se utilizará para contar los tweets por usuario
tweets_por_usuario = {}
# diccionario que se utilizara para contar los tweets por fecha
tweets_por_fecha = {}
# diccionario que se utilizara para contar los usuarios que twittean por fecha
usuarios_por_fecha = {}
# lista de id de usuarios que twittean por día
lista_user = []
fecha = ''

"""*****************************ESCRIBIR EN EL FICHERO 1*******************************"""
try:
    # para cada uno de los tweets recuperados
    for tweet in all_tweets:
        # try:#es un ReTweet
         #   fichero.write(tweet.retweeted_status.full_text + os.linesep)
        #except:#no es un ReTweet
         #   fichero.write(tweet.full_text + os.linesep)
        if tweet.full_text.startswith('RT'):
            continue
        fichero_all_tweets.write(tweet.full_text + os.linesep)
        # linea de separacion de tweets
        fichero_all_tweets.write("-------------" + os.linesep)
        # Aqui se cuentan los tweets por usuario
        tweets_por_usuario[tweet.user.name] = tweets_por_usuario.get(tweet.user.name, 0) + 1
        # Aqui se cuentan los tweets por fecha
        tweets_por_fecha[tweet.created_at.strftime('%d-%m-%y')] = tweets_por_fecha.get(tweet.created_at.strftime('%d-%m-%y'), 0) + 1
        if tweet.created_at.strftime('%d-%m-%y') != fecha:
            # si no es la misma fecha quiere decir que la API nos comienza a traer tweets de otro dia
            lista_user.clear()
            # actualizamos la fecha
            fecha = tweet.created_at.strftime('%d-%m-%y')
            # agregamos por primera vez el id del user que leemos
            lista_user.append(tweet.user.id)
            # contamos su tweet
            usuarios_por_fecha[tweet.created_at.strftime('%d-%m-%y')] = usuarios_por_fecha.get(tweet.created_at.strftime('%d-%m-%y'), 0) + 1
        else: # seguimos en la misma fecha
            if tweet.user.id not in lista_user: # solo contamos su tweet si no ha tweeteado antes en el mismo dia
                # por ende ya lo listamos en los que han tweeteado hoy
                lista_user.append(tweet.user.id)
                # contamos su tweet
                usuarios_por_fecha[tweet.created_at.strftime('%d-%m-%y')] = usuarios_por_fecha.get(tweet.created_at.strftime('%d-%m-%y'), 0) + 1

finally:# procedemos a cerrar el archivo
    fichero_all_tweets.close()



"""*****************************ESCRIBIR EN EL FICHERO 5*****************************"""
fichero_5 = open('conjunto_5.txt', 'w', encoding='utf-8')

fechas_ordenadas = sorted(tweets_por_fecha, key=tweets_por_fecha.get, reverse=True)

for fecha in fechas_ordenadas:
    fichero_5.write(fecha + ":" + str(tweets_por_fecha[fecha]) + "\n")

fichero_5.close()


"""*****************************ESCRIBIR EN EL FICHERO 6*****************************"""

fichero_6 = open('conjunto_6.txt', 'w', encoding='utf-8')

# con esto ordenamos el diccionario por valor
fechas = sorted(usuarios_por_fecha, key=usuarios_por_fecha.get, reverse=True)

# ahora necesitamos escribir los valores ordenados pero con los valores correspondientes
for fecha in fechas:
    fichero_6.write(fecha + ":" + str(usuarios_por_fecha[fecha]) + "\n")

fichero_6.close()


"""*****************************ESCRIBIR EN EL FICHERO 7*****************************"""

fichero_7 = open('conjunto_7.txt', 'w', encoding='utf-8')

# con esto ordenamos el diccionario por valor
usuarios = sorted(tweets_por_usuario, key=tweets_por_usuario.get, reverse=True)
# ahora necesitamos escribir los valores ordenados pero con los valores correspondientes
for usuario in usuarios:
    fichero_7.write(usuario + ":" + str(tweets_por_usuario[usuario]) + "\n")

fichero_7.close()


"""****************MOSTRAMOS EL HISTOGRAMA DE TWEETS POR FECHA****************"""
grafico = pandas.DataFrame.from_dict(tweets_por_fecha, orient='index')

grafico.plot(kind='bar')
plot.title('Numero de tweets por fecha')

plot.show()


"""********MOSTRAMOS EL HISTOGRAMA DE USUARIOS QUE TWEETEARON POR DIA**********"""
grafico = pandas.DataFrame.from_dict(usuarios_por_fecha, orient='index')

grafico.plot(kind='bar')
plot.title('Usuarios que tweetearon por fecha')

plot.show()


"""****************MOSTRAMOS EL HISTOGRAMA DE TWEETS POR USUARIO****************"""
grafico = pandas.DataFrame.from_dict(tweets_por_usuario, orient='index')

grafico.plot(kind='bar')
plot.title('Numero de tweets por usuario')

plot.show()



"""*****************************ESCRIBIR EN EL FICHERO 2*******************************"""
try:
    # para cada uno de los tweets recuperados
    for tweet in tweets:
        # try:#es un ReTweet
         #   fichero.write(tweet.retweeted_status.full_text + os.linesep)
        # except:#no es un ReTweet
         #   fichero.write(tweet.full_text + os.linesep)
        if tweet.full_text.startswith('RT'):
            continue
        fichero_tweets.write(tweet.full_text + os.linesep)
        # linea de separacion de tweets
        fichero_tweets.write("-------------" + os.linesep)
finally:# procedemos a cerrar el archivo
    fichero_tweets.close()


"""*******************************PARAMETROS UTILIZADOS*******************************"""
# declaramos un diccionario vacio que contendra las palabras mas comunes
tendencias_all_tweets = {}
tendencias_tweets = {}
# palabras excluidas
palabras_excluidas = [
    'el', 'la', 'los', 'las', 'un', 'una', 'unos', 'unas', 'al', 'del', 'lo', 'le', 'y',
    'e', 'o', 'u', 'de', 'a', 'en', 'que', 'es', 'por', 'para', 'con', 'se', 'su', 'les',
    'me', 'q', 'te', 'pero', 'mi', 'ya', 'cuando', 'como', 'estoy', 'voy', 'porque', 'he',
    'son', 'solo', 'tengo', 'muy', 'no', 'ni', '-------------', ',', '.', ';', ':',
    'Yolanda', 'Park', 'yolanda', 'park', 'tu', 'sus', 'si', '-', 'park,', 'vos'
]

"""***************************RECUPERAR INFORMACION DEL FICHERO 1*******************************"""
try:
    # abrimos el fichero para leerlo
    fichero_all_tweets = open('conjunto_1.txt', 'r', encoding='utf-8')
    for linea in fichero_all_tweets:
        palabras = linea.strip().lower().split()
        for palabra in palabras:
            if (palabra not in palabras_excluidas) \
                    and (palabra[0] != "@") \
                    and (palabra[0:4] != 'http') \
                    and (palabra not in emoji.UNICODE_EMOJI_SPANISH): #que no comience por @ o http o hayan emojis
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


"""****************MOSTRAMOS EL HISTOGRAMA DE PALABRAS DEL CONJUNTO 1****************"""
grafico = pandas.DataFrame.from_dict(tendencias_all_tweets, orient='index')
grafico.plot(kind='bar')
plot.title('Palabras del conjunto de tweets 1')
plot.show()
# plot.savefig('histograma_1.png')


"""***************************RECUPERAR INFORMACION DEL FICHERO 2*******************************"""
try:
    # abrimos el fichero para leerlo
    fichero_tweets = open('conjunto_2.txt', 'r', encoding='utf-8')
    for linea in fichero_tweets:
        palabras = linea.strip().lower().split()
        for palabra in palabras:
            if (palabra not in palabras_excluidas) \
                    and (palabra[0] != "@") \
                    and (palabra[0:4] != 'http') \
                    and (palabra not in emoji.UNICODE_EMOJI_SPANISH):
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


"""****************MOSTRAMOS EL HISTOGRAMA DE PALABRAS DEL CONJUNTO 2****************"""
grafico = pandas.DataFrame.from_dict(tendencias_tweets, orient='index')
grafico.plot(kind='bar')
plot.title('Palabras del conjunto de tweets 2')
plot.show()
# plot.savefig('histograma_2.png')

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


for palabra in claves_1:
    if palabra in claves_2:
        # como esta contenida en claves_1 y claves_2 forma parte de la interseccion
        interseccion.append(palabra)
    else:
        #contenido en 1 pero no en 2
        uno_no_dos.append(palabra)

for palabra in claves_2:
    if palabra not in claves_1:
        # palabra del conjunto 2 que no pertenece al conjunto 1
        dos_no_uno.append(palabra)

"""*****************************BUSCAR LEN()>=2*****************************"""
fichero_3 = open('conjunto_3.txt', 'w', encoding='utf-8')

for palabra in interseccion:
    if len(palabra) >= 2:
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

"""*****************************BUSCAR LEN()>=2*****************************"""
fichero_4 = open('conjunto_4.txt', 'w', encoding='utf-8')

for palabra in union:
    if len(palabra) >= 2:
        fichero_4.write(palabra + os.linesep)

fichero_4.close()
