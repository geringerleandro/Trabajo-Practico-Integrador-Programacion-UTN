diccionario_paises=[]
with open ('paises.csv', 'r', encoding="utf-8" ) as archivo:
    encabezado=next(archivo)
    for linea in archivo:
        linea_procesada=linea.strip().split(",")
        linea_paises={'nombre': linea_procesada[0], 'poblacion': linea_procesada[1], 'superficie': linea_procesada[2], 'continente':linea_procesada[3]}
        diccionario_paises.append(linea_paises)
