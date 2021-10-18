# libreria de python que facilita el uso de la API de twitter
import tweepy as tw
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