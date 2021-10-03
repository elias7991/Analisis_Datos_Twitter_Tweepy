#libreria de python que facilita el uso de la API de twitter
import tweepy as tw
#libreria que se utilizara para recuperar la fecha actual
from datetime import datetime
#libreria que se utiliza para dar el salto de linea al escribir en el archivo
import os
#libreria que contiene los emojis UNICODE
import emoji

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

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
"""
    **************************Definicion de clase API**************************
    class tweepy.API( auth = None , * , cache = None , host = 'api.twitter.com' , 
    parser = None , proxy = None , retry_count = 0 , retry_delay = 0 , 
    retry_errors = None , timeout = 60 , upload_host = 'upload. twitter.com ' , 
    user_agent = Ninguno , wait_on_rate_limit =Falso )
"""
"""
    con el argumento True de wait_on_rate_limit podemos hacer que nuestro programa espere a tener
    cupo de descarga nuevamente y que no termine de ejecutarse.
"""
api = tw.API(auth, wait_on_rate_limit=True)


"""********************************PARÁMETROS DE BÚSQUEDA****************************"""
#definimos la palabra y/o frase que vamos a buscar o una lista para iterar despues
"""*******************************ESTA MAL*************************************"""
search_word = "*"
"""****************************************************************************"""
#trae la fecha de hoy en formato de cadena
today = datetime.today().strftime('%Y-%m-%d')
#asignamos la fecha de hoy para buscar los tweets más actuales siempre
date_until = today
#definimos el número máximo de tweets que vamos a buscar
max_tweets = 100


"""******************************RECUPERACION DE TWEETS******************************"""
tweets = tw.Cursor(
    api.search_tweets,
    #q, de query
    q=search_word,
    lang="es",
    until=date_until,
    #para traer el tweet completo sin truncar en el caracter 140
    tweet_mode="extended"
).items(max_tweets)


"""*************************PREPARAR EL FICHERO A UTILIZAR***************************"""
fichero = open('conjunto_1.txt', 'w', encoding="utf-8")


"""*****************************ESCRIBIR EN EL FICHERO*******************************"""
try:
    #para cada uno de los tweets recuperados
    for tweet in tweets:
        #try:#es un ReTweet
         #   fichero.write(tweet.retweeted_status.full_text + os.linesep)
        #except:#no es un ReTweet
         #   fichero.write(tweet.full_text + os.linesep)
        if tweet.full_text.startswith('RT'):
            continue
        fichero.write(tweet.full_text + os.linesep)
        #linea de separacion de tweets
        fichero.write("-------------" + os.linesep)
finally:#procedemos a cerrar el archivo
    fichero.close()


"""*******************************PARAMETROS UTILIZADOS*******************************"""
#declaramos un diccionario vacio que contendra las palabras mas comunes
tendencias = {}
#palabras excluidas
palabras_excluidas = [
    'el', 'la', 'los', 'las', 'un', 'una', 'unos', 'unas', 'al', 'del', 'lo', 'le', 'y',
    'e', 'o', 'u', 'de', 'a', 'en', 'que', 'es', 'por', 'para', 'con', 'se', 'su', 'les',
    'me', 'q', 'te', 'pero', 'mi', 'ya', 'cuando', 'como', 'estoy', 'voy', 'porque', 'he',
    'son', 'solo', 'tengo', 'muy', 'no', 'ni', '-------------'
]


"""********************************LEER EL FICHERO***********************************"""
#abrimos el fichero para leerlo
fichero = open('conjunto_1.txt', 'r', encoding='utf-8')
for linea in fichero:
    palabras = linea.strip().lower().split()
    for palabra in palabras:
        if (palabra not in palabras_excluidas) \
        and (palabra[0] != "@") \
        and (palabra[0:4] != 'http') \
        and (palabra not in emoji.UNICODE_EMOJI_SPANISH):
            tendencias[palabra] = tendencias.get(palabra, 0) + 1

for key in tendencias:
    print(key, ": ", tendencias[key])

