# libreria de expresiones regulares de python
import re
import emoji


"""*************************FICHEROS QUE CONTIENEN TEXTO NO LIMPIO***************************"""
fichero_all_tweets = open('conjunto_1.txt', 'r', encoding="utf-8")
fichero_tweets = open('conjunto_2.txt', 'r', encoding="utf-8")


"""*************************FICHEROS QUE CONTENDRAN TEXTO LIMPIO***************************"""
texto_limpio_all = open('conjunto_1_limpio.txt', 'w', encoding="utf-8")
texto_limpio = open('conjunto_2_limpio.txt', 'w', encoding="utf-8")


"""*************************LIMPIEZA DEL TXT DEL CONJUNTO1 DE TWEETS*************************"""
try:
    for linea in fichero_all_tweets:
        # elimina todos los digitos contenidos en el archivo de texto
        linea_limpia = re.sub('\d','',linea)
        #linea_limpia = ''.join([i for i in linea_limpia if i not in emoji.UNICODE_EMOJI_SPANISH])
        # elimina toda codifcacion unicode de emoticonos que encuentre
        linea_limpia = re.sub(pattern="["
                            u"\U00010000-\U0001FFFF"
                                               "]+", repl='', string=linea_limpia, flags=re.UNICODE)
        # elimina todas las url
        linea_limpia = re.sub(r'http\S+', '', linea_limpia)
        # elimina todas las menciones
        linea_limpia = re.sub(r'@\S+', '', linea_limpia)
        # elimina todos los hashtag
        linea_limpia = re.sub(r'#\S+', '', linea_limpia)
        # elimina todos los simbolos que no nos interesan
        linea_limpia = re.sub(r'[.,;:¿?_+/%!"$&()=-]', '', linea_limpia)
        texto_limpio_all.write(linea_limpia)
finally:
    fichero_all_tweets.close()
    texto_limpio_all.close()


"""*************************LIMPIEZA DEL TXT DEL CONJUNTO2 DE TWEETS*************************"""
try:
    for linea in fichero_tweets:
        # elimina todos los digitos contenidos en el archivo de texto
        linea_limpia = re.sub('\d','',linea)
        #linea_limpia = ''.join([i for i in linea_limpia if i not in emoji.UNICODE_EMOJI_SPANISH])
        # elimina toda codifcacion unicode de emoticonos que encuentre
        linea_limpia = re.sub(pattern="["
                            u"\U00010000-\U0001FFFF"
                                               "]+", repl='', string=linea_limpia, flags=re.UNICODE)
        # elimina todas las url
        linea_limpia = re.sub(r'http\S+', '', linea_limpia)
        # elimina todas las menciones
        linea_limpia = re.sub(r'@\S+', '', linea_limpia)
        # elimina todos los hashtag
        linea_limpia = re.sub(r'#\S+', '', linea_limpia)
        # elimina todos los simbolos que no nos interesan
        linea_limpia = re.sub(r'[.,;:¿?_+/%!"$&()=-]', '', linea_limpia)
        texto_limpio.write(linea_limpia)
finally:
    fichero_tweets.close()
    texto_limpio.close()