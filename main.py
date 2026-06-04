from funciones import valida_nombre,valida_continente,numero_entero_positivo


diccionario_paises=[]
with open ('paises.csv', 'r', encoding="utf-8" ) as archivo:
    encabezado=next(archivo)
    for linea in archivo:
        linea_procesada=linea.strip().split(",")
        linea_paises={'nombre': linea_procesada[0], 'poblacion': linea_procesada[1], 'superficie': linea_procesada[2], 'continente':linea_procesada[3]}
        diccionario_paises.append(linea_paises)

ingreso_menu = True

while ingreso_menu:
    print("Menu:")
    print("1- Agregar pais")
    print("2- Actualizar poblacion")
    print("3- Buscar pais por nombre.")
    print("4- Filtrar paises.")
    print("5- Ordenar paises.")
    print("6- Mostrar estadisticas.")
    print("7- Salir.")

    opcion = numero_entero_positivo("Ingrese opcion: ")

    match opcion:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass
        case 7:
            print("Saliendo....")
            ingreso_menu = False
            break


