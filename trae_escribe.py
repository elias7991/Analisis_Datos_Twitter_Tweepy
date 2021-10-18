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
        # como no queremos los RT
        if tweet.full_text.startswith('RT'):
            continue
        fichero_all_tweets.write("- " + tweet.full_text + os.linesep)
        tweets_por_usuario[tweet.user.name] = tweets_por_usuario.get(tweet.user.name, 0) + 1
        # Aqui se cuentan los tweets por fecha
        tweets_por_fecha[tweet.created_at.strftime('%d-%m-%y')] = tweets_por_fecha.get(
            tweet.created_at.strftime('%d-%m-%y'), 0) + 1
        if tweet.created_at.strftime('%d-%m-%y') != fecha:
            # si no es la misma fecha quiere decir que la API nos comienza a traer tweets de otro dia
            lista_user.clear()
            # actualizamos la fecha
            fecha = tweet.created_at.strftime('%d-%m-%y')
            # agregamos por primera vez el id del user que leemos
            lista_user.append(tweet.user.id)
            # contamos su tweet
            usuarios_por_fecha[tweet.created_at.strftime('%d-%m-%y')] = usuarios_por_fecha.get(
                tweet.created_at.strftime('%d-%m-%y'), 0) + 1
        else:  # seguimos en la misma fecha
            if tweet.user.id not in lista_user:  # solo contamos su tweet si no ha tweeteado antes en el mismo dia
                # por ende ya lo listamos en los que han tweeteado hoy
                lista_user.append(tweet.user.id)
                # contamos su tweet
                usuarios_por_fecha[tweet.created_at.strftime('%d-%m-%y')] = usuarios_por_fecha.get(
                    tweet.created_at.strftime('%d-%m-%y'), 0) + 1

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
