import tweepy as tw
from autenticacion import api
# libreria que se utilizara para recuperar la fecha actual
import datetime
import os

"""********************************PARÁMETROS DE BÚSQUEDA****************************"""
# definimos la palabra y/o frase que vamos a buscar o una lista para iterar despues
search_word = "Berizzo"
# trae la fecha de hoy en formato de cadena
today = datetime.datetime.today().strftime('%Y-%m-%d')
# fecha de la semana pasada
last_week = (datetime.datetime.today() - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
# definimos el número máximo de tweets que vamos a buscar
max_tweets = 20

"""
    **********************************************************************************
    ******************************RECUPERACION DE TWEETS******************************
    **********************************************************************************
"""

"""***********************************CONJUNTO 1 DE TWEETS****************************"""
"""***********************************SIN QUERY PARTICULAR****************************"""
all_tweets = tw.Cursor(
    api.search_tweets,
    q="* since:"+last_week+" until:"+today,
    lang="es",
    tweet_mode="extended"
).items(max_tweets)

"""***********************************CONJUNTO 2 DE TWEETS***************************"""
"""***********************************CON UNA QUERY**********************************"""
tweets = tw.Cursor(
    api.search_tweets,
    # q, de query
    q=search_word+" since:"+last_week+" until:"+today,
    lang="es",
    # para traer el tweet completo sin truncar en el caracter 140
    tweet_mode="extended"
).items(max_tweets)

"""*************************PREPARAR LOS FICHEROS A UTILIZAR***************************"""
fichero_all_tweets = open('conjunto_1.txt', 'w', encoding="utf-8")
fichero_tweets = open('conjunto_2.txt', 'w', encoding="utf-8")


"""*****************************ESCRIBIR EN EL FICHERO 1*******************************"""
try:
    # para cada uno de los tweets recuperados
    for tweet in all_tweets:
        # como no queremos los RT
        if tweet.full_text.startswith('RT'):
            continue
        fichero_all_tweets.write("- " + tweet.full_text + os.linesep)
finally:# procedemos a cerrar el archivo
    fichero_all_tweets.close()

"""*****************************ESCRIBIR EN EL FICHERO 2*******************************"""
try:
    # para cada uno de los tweets recuperados
    for tweet in tweets:
        # como no queremos los RT
        if tweet.full_text.startswith('RT'):
            continue
        fichero_tweets.write("- " + tweet.full_text + os.linesep)
finally:# procedemos a cerrar el archivo
    fichero_tweets.close()