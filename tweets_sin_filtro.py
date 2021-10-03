#libreria de python que facilita el uso de la API de twitter
import tweepy as tw
#libreria que se utilizara para recuperar la fecha actual
from datetime import datetime
#libreria que se utiliza para dar el salto de linea al escribir en el archivo
import os

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
user = tw.Client(auth, wait_on_rate_limit=True)

tweets = user.search_all_tweets(query="q", max_results=10)

for tweet in tweets:
    print(tweet)
