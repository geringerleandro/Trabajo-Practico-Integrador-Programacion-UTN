from funciones import valida_nombre,valida_continente,numero_entero_positivo,filtrar_por_continente,filtrar_por_rango_poblacion,filtrar_por_superficie


diccionario_paises=[]
with open ('paises.csv', 'r', encoding="utf-8" ) as archivo:
    encabezado=next(archivo)
    for linea in archivo:
        linea_procesada=linea.strip().split(",")
        linea_paises={
            'nombre': linea_procesada[0],
            'poblacion': int(linea_procesada[1]),
            'superficie': int(linea_procesada[2]),
            'continente':linea_procesada[3]
            }
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
            print("Menu:")
            print("1- Filtrar por continente.")
            print("2- Filtrar por rango de poblacion.")
            print("3- Filtrar por rango de superficie.")

            opcion = numero_entero_positivo("Ingrese opcion: ")

            match opcion:
                case 1:
                    continente = input("Ingrese continente: ")
                    resultado = filtrar_por_continente(diccionario_paises, continente)
                    if len(resultado)== 0:
                        print("No se han encontrado paises para dicho continente")
                    else:
                        print(f"\nPaises de {continente}:\n")
                        for pais in resultado:
                            print(pais["nombre"])
                case 2:
                    minimo = numero_entero_positivo("Ingrese poblacion minima: ")
                    maximo = numero_entero_positivo("Ingrese poblacion maxima: ")

                    resultado = filtrar_por_rango_poblacion(diccionario_paises, minimo, maximo)

                    if len(resultado) == 0:
                        print("No se encontraron paises en ese rango.")
                    else:
                        for pais in resultado:
                            print(f"{pais["nombre"]} - {pais["poblacion"]}")
                case 3:
                    minimo = numero_entero_positivo("Ingrese superficie minima: ")
                    maximo = numero_entero_positivo("Ingrese superficie maxima: ")

                    resultado = filtrar_por_superficie(diccionario_paises, minimo, maximo)

                    if len(resultado) == 0:
                        print("No se encontraron paises en ese rango.")
                    else:
                        for pais in resultado:
                            print(f"{pais["nombre"]} - {pais["superficie"]}")
        case 5:
            pass
        case 6:
            pass
        case 7:
            print("Saliendo....")
            ingreso_menu = False
            break


