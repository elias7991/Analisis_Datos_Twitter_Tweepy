import pandas
import numpy as np
import matplotlib.pyplot as plot
from trae_escribe import tweets_por_fecha, usuarios_por_fecha, tweets_por_usuario
from contar_palabras import tendencias_all_tweets, tendencias_tweets, interseccion, uno_no_dos, uno_no_dos_y, dos_no_uno, dos_no_uno_y, union, union_y


"""****************GRAFICO DEL ITEM 1****************"""
"""****************MOSTRAMOS EL HISTOGRAMA DE PALABRAS DEL CONJUNTO 1****************"""
if (len(tendencias_all_tweets.keys()) <= 20):
    grafico = pandas.DataFrame.from_dict(tendencias_all_tweets, orient='index')
    grafico.plot(kind='bar')
    plot.title('Grafico item 1')
    plot.show()
    # plot.savefig('histograma_1.png')
else:
    # con esto ordenamos el diccionario por valor
    mas_usadas = sorted(tendencias_all_tweets, key=tendencias_all_tweets.get, reverse=True)
    top20 = []
    top20_y = []
    i = 0
    while i < 20:
        top20.append(mas_usadas[i])
        top20_y.append(tendencias_all_tweets[mas_usadas[i]])
        i = i + 1
    plot.bar(top20, top20_y)
    # Legenda en el eje y
    plot.ylabel('Frecuencia Absoluta')
    # Legenda en el eje x
    plot.xlabel('Palabras')
    # Título de Gráfica
    plot.title('Grafico item 1')
    plot.xticks(rotation=90)
    ## Mostramos Gráfica
    plot.show()

"""****************GRAFICO DEL ITEM 2****************"""
"""****************MOSTRAMOS EL HISTOGRAMA DE PALABRAS DEL CONJUNTO 2****************"""
if (len(tendencias_tweets.keys())<=20):
    grafico = pandas.DataFrame.from_dict(tendencias_tweets, orient='index')
    grafico.plot(kind='bar')
    plot.title('Grafico item 2')
    plot.show()
    # plot.savefig('histograma_2.png')
else:
    # con esto ordenamos el diccionario por valor
    mas_usadas = sorted(tendencias_tweets, key=tendencias_tweets.get, reverse=True)
    top20 = []
    top20_y = []
    i = 0
    while i < 20:
        top20.append(mas_usadas[i])
        top20_y.append(tendencias_tweets[mas_usadas[i]])
        i = i + 1
    plot.bar(top20, top20_y)
    # Legenda en el eje y
    plot.ylabel('Frecuencia Absoluta')
    # Legenda en el eje x
    plot.xlabel('Palabras')
    # Título de Gráfica
    plot.title('Grafico item 2')
    plot.xticks(rotation=90)
    ## Mostramos Gráfica
    plot.show()


"""****************GRAFICO DEL ITEM 3****************"""
"""****************MOSTRAMOS EL HISTOGRAMA DE PALABRAS EN LA INTERSECCION****************"""
if len(interseccion)<=20:
    n = len(interseccion)
    lista_aux = []
    # numero de repeticiones en el conjunto 1
    serie_1 = []
    # numero de repeticiones en el conjunto 2
    serie_2 = []
    # creamos la lista auxiliar
    for palabra in interseccion:
        # aqui se guarda la palabra seguido de cuantas veces se repite en el item 1 y en el item 2
        lista_aux.append([palabra, tendencias_all_tweets[palabra], tendencias_tweets[palabra]])
    # ordenamos la lista por la frecuencia absoluta neta
    # frecuencia neta = frecuencia absoluta en 1 + frecuencia absoluta en 2
    for i in range(len(interseccion) - 1):
        for j in range(i + 1, len(interseccion)):
            if (lista_aux[i][1] + lista_aux[i][2]) < (lista_aux[j][1] + lista_aux[j][2]):
                # salvamos el valor en j
                aux = lista_aux[j]
                # llevamos lo que hay en i a j
                lista_aux[j] = lista_aux[i]
                # completamos el swap
                lista_aux[i] = aux
    # aqui se cargan las frecuencias absolutas de cada serie de datos
    for i in range(n):
        serie_1.append(lista_aux[i][1])
        serie_2.append(lista_aux[i][2])

    numero_de_grupos = len(serie_1)
    indice_barras = np.arange(numero_de_grupos)
    ancho_barras = 0.35

    plot.bar(indice_barras, serie_1, width=ancho_barras, label='Conjunto1')
    plot.bar(indice_barras + ancho_barras, serie_2, width=ancho_barras, label='Conjunto2')
    plot.legend(loc='best')
    ## Se colocan los indicadores en el eje x
    plot.xticks(indice_barras + ancho_barras, (lista_aux[i][0] for i in range(n)), rotation=90)
    plot.ylabel('Frecuencia Absoluta')
    plot.xlabel('Palabras')
    plot.title('Grafico item 3 - Interseccion de Palabras')
    plot.show()
else: #buscar los 20 con frecuencia absoluta más alta
    lista_aux = []
    # numero de repeticiones en el conjunto 1
    serie_1 = []
    # numero de repeticiones en el conjunto 2
    serie_2 = []
    # creamos la lista auxiliar
    for palabra in interseccion:
        # aqui se guarda la palabra seguido de cuantas veces se repite en el item 1 y en el item 2
        lista_aux.append([palabra, tendencias_all_tweets[palabra], tendencias_tweets[palabra]])
    # ordenamos la lista por la frecuencia absoluta neta
    # frecuencia neta = frecuencia absoluta en 1 + frecuencia absoluta en 2
    for i in range(len(interseccion) - 1):
        for j in range(i + 1, len(interseccion)):
            if (lista_aux[i][1] + lista_aux[i][2]) < (lista_aux[j][1] + lista_aux[j][2]):
                # salvamos el valor en j
                aux = lista_aux[j]
                # llevamos lo que hay en i a j
                lista_aux[j] = lista_aux[i]
                # completamos el swap
                lista_aux[i] = aux
    # aqui se cargan las frecuencias absolutas de cada serie de datos
    for i in range(20):
        serie_1.append(lista_aux[i][1])
        serie_2.append(lista_aux[i][2])

    numero_de_grupos = len(serie_1)
    indice_barras = np.arange(numero_de_grupos)
    ancho_barras = 0.35

    plot.bar(indice_barras, serie_1, width=ancho_barras, label='Conjunto1')
    plot.bar(indice_barras + ancho_barras, serie_2, width=ancho_barras, label='Conjunto2')
    plot.legend(loc='best')
    ## Se colocan los indicadores en el eje x
    plot.xticks(indice_barras + ancho_barras, (lista_aux[i][0] for i in range(20)), rotation=90)
    plot.ylabel('Frecuencia Absoluta')
    plot.xlabel('Palabras')
    plot.title('Grafico item 3 - Interseccion de Palabras')
    plot.show()

"""****************GRAFICO DEL ITEM 4****************"""
"""****************MOSTRAMOS EL HISTOGRAMA DE PALABRAS EN LA UNION****************"""
if len(union)<=20:
    dicc_aux = {}
    # creamos la lista auxiliar
    for palabra in union:
        if tendencias_all_tweets[palabra]:
            dicc_aux[palabra] = dicc_aux.get(palabra, 0) + tendencias_all_tweets[palabra]
        if tendencias_tweets[palabra]:
            dicc_aux[palabra] = dicc_aux.get(palabra, 0) + tendencias_tweets[palabra]

    grafico = pandas.DataFrame.from_dict(dicc_aux, orient='index')
    grafico.plot(kind='bar')
    plot.title('Grafico item 4 - Palabras en la Union')
    plot.show()
else:
    # ordenamos las listas
    for i in range(len(union_y)-1):
        for j in range(i+1, len(union_y)):
            if(union_y[i]<union_y[j]):
                aux_num = union_y[i]
                aux_pal = union[i]
                union_y[i] = union_y[j]
                union[i] = union[j]
                union_y[j] = aux_num
                union[j] = aux_pal
    # solo usamos el top 20
    plot.bar([union[i] for i in range(20)], [union_y[i] for i in range(20)])
    # Legenda en el eje y
    plot.ylabel('Frecuencia Absoluta Neta (1+2)')
    # Legenda en el eje x
    plot.xlabel('Palabras')
    # Título de Gráfica
    plot.title('Grafico item 4 - Palabras en la Union')
    plot.xticks(rotation=90)
    ## Mostramos Gráfica
    plot.show()

"""****************GRAFICO DEL ITEM 5****************"""
"""****************MOSTRAMOS EL HISTOGRAMA DE TWEETS POR FECHA****************"""
if (len(tweets_por_fecha.keys()) <= 20):
    grafico = pandas.DataFrame.from_dict(tweets_por_fecha, orient='index')
    grafico.plot(kind='bar')
    plot.title('Grafico item 5 - Numero de tweets por fecha')
    plot.show()
else:
    # con esto ordenamos el diccionario por valor
    mas_usadas = sorted(tweets_por_fecha, key=tweets_por_fecha.get, reverse=True)
    top20 = []
    top20_y = []
    i = 0
    while i < 20:
        top20.append(mas_usadas[i])
        top20_y.append(tweets_por_fecha[mas_usadas[i]])
        i = i + 1
    plot.bar(top20, top20_y)
    # Legenda en el eje y
    plot.ylabel('Numero de tweets')
    # Legenda en el eje x
    plot.xlabel('Fechas')
    # Título de Gráfica
    plot.title('Grafico item 5 - Numero de tweets por fecha')
    plot.xticks(rotation=90)
    ## Mostramos Gráfica
    plot.show()


"""****************GRAFICO DEL ITEM 6****************"""
"""********MOSTRAMOS EL HISTOGRAMA DE USUARIOS QUE TWEETEARON POR DIA**********"""
if (len(usuarios_por_fecha.keys()) <= 20):
    grafico = pandas.DataFrame.from_dict(usuarios_por_fecha, orient='index')
    grafico.plot(kind='bar')
    plot.title('Grafico item 6 - Usuarios que twittearon por fecha')
    plot.show()
else:
    # con esto ordenamos el diccionario por valor
    mas_usadas = sorted(usuarios_por_fecha, key=usuarios_por_fecha.get, reverse=True)
    top20 = []
    top20_y = []
    i = 0
    while i < 20:
        top20.append(mas_usadas[i])
        top20_y.append(usuarios_por_fecha[mas_usadas[i]])
        i = i + 1
    plot.bar(top20, top20_y)
    # Legenda en el eje y
    plot.ylabel('Numero de usuarios')
    # Legenda en el eje x
    plot.xlabel('Fechas')
    # Título de Gráfica
    plot.title('Grafico item 6 - Usuarios que twittearon por fecha')
    plot.xticks(rotation=90)
    ## Mostramos Gráfica
    plot.show()


"""****************GRAFICO DEL ITEM 7****************"""
"""****************MOSTRAMOS EL HISTOGRAMA DE TWEETS POR USUARIO****************"""
if (len(tweets_por_usuario.keys()) <= 20):
    grafico = pandas.DataFrame.from_dict(tweets_por_usuario, orient='index')
    grafico.plot(kind='bar')
    plot.title('Grafico item 7 - Numero de tweets por usuario')
    plot.show()
else:
    # con esto ordenamos el diccionario por valor
    mas_usadas = sorted(tweets_por_usuario, key=tweets_por_usuario.get, reverse=True)
    top20 = []
    top20_y = []
    i = 0
    while i < 20:
        top20.append(mas_usadas[i])
        top20_y.append(tweets_por_usuario[mas_usadas[i]])
        i = i + 1
    plot.bar(top20, top20_y)
    # Legenda en el eje y
    plot.ylabel('Numero de tweets')
    # Legenda en el eje x
    plot.xlabel('Usuarios')
    # Título de Gráfica
    plot.title('Grafico item 7 - Numero de tweets por usuario')
    plot.xticks(rotation=90)
    ## Mostramos Gráfica
    plot.show()


"""****************GRAFICO DEL ITEM 8****************"""
"""****************MOSTRAMOS EL HISTOGRAMA DE PALABRAS UNICAS POR CONJUNTO****************"""
"""****************GRAFICO DEL CONJUNTO 1 MENOS EL CONJUNTO 2****************"""
if(len(uno_no_dos)<=20):
    plot.bar(uno_no_dos, uno_no_dos_y, align='center')
    plot.xlabel('Palabras')
    plot.ylabel('Frecuencia Absoluta')
    plot.title('Grafico item 8 - Conjunto 1 menos 2')
    plot.xticks(rotation=90)
    plot.show()
else:
    # ordenamos las listas
    for i in range(len(uno_no_dos_y) - 1):
        for j in range(i + 1, len(uno_no_dos_y)):
            if (uno_no_dos_y[i] < uno_no_dos_y[j]):
                aux_num = uno_no_dos_y[i]
                aux_pal = uno_no_dos[i]
                uno_no_dos_y[i] = uno_no_dos_y[j]
                uno_no_dos[i] = uno_no_dos[j]
                uno_no_dos_y[j] = aux_num
                uno_no_dos[j] = aux_pal
    # solo usamos el top 20
    plot.bar([uno_no_dos[i] for i in range(20)], [uno_no_dos_y[i] for i in range(20)])
    # Legenda en el eje y
    plot.ylabel('Frecuencia Absoluta')
    # Legenda en el eje x
    plot.xlabel('Palabras')
    # Título de Gráfica
    plot.title('Grafico item 8 - Conjunto 1 menos 2')
    plot.xticks(rotation=90)
    ## Mostramos Gráfica
    plot.show()


"""****************GRAFICO DEL CONJUNTO 2 MENOS EL CONJUNTO 1****************"""
if(len(dos_no_uno)<=20):
    plot.bar(dos_no_uno, dos_no_uno_y, align='center')
    plot.xlabel('Palabras')
    plot.ylabel('Frecuencia Absoluta')
    plot.title('Grafico item 8 - Conjunto 2 menos 1')
    plot.xticks(rotation=90)
    plot.show()
else:
    # ordenamos las listas
    for i in range(len(dos_no_uno_y) - 1):
        for j in range(i + 1, len(dos_no_uno_y)):
            if (dos_no_uno_y[i] < dos_no_uno_y[j]):
                aux_num = dos_no_uno_y[i]
                aux_pal = dos_no_uno[i]
                dos_no_uno_y[i] = dos_no_uno_y[j]
                dos_no_uno[i] = dos_no_uno[j]
                dos_no_uno_y[j] = aux_num
                dos_no_uno[j] = aux_pal
    # solo usamos el top 20
    plot.bar([dos_no_uno[i] for i in range(20)], [dos_no_uno_y[i] for i in range(20)])
    # Legenda en el eje y
    plot.ylabel('Frecuencia Absoluta')
    # Legenda en el eje x
    plot.xlabel('Palabras')
    # Título de Gráfica
    plot.title('Grafico item 8 - Conjunto 2 menos 1')
    plot.xticks(rotation=90)
    ## Mostramos Gráfica
    plot.show()