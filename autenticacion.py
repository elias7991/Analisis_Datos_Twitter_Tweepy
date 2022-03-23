# libreria de python que facilita el uso de la API de twitter
import tweepy as tw
"""
**********************************************************************************************************
************************************AUTENTICACION CON PROTOCOLO OAuth2************************************
**********************************************************************************************************
"""

"""*************************************VARIABLES DE AUTENTICACION*************************************"""
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
"""************************************AUTENTICACION***************************************************"""
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
"""
    con el argumento True de wait_on_rate_limit podemos hacer que nuestro programa espere a tener
    cupo de descarga nuevamente y que no termine de ejecutarse.
"""
api = tw.API(auth, wait_on_rate_limit=True)
