
from funciones import valida_nombre,valida_continente,numero_entero_positivo,filtrar_por_continente,filtrar_por_rango_poblacion,filtrar_por_superficie,ordenar_paises,ordenar_por_poblacion,superficie_menor_a_mayor,superficie_mayor_a_menor,mayor_y_menor_poblacion,promedio_poblacion,promedio_superficie_continente,quitar_acentos,paises_en_continente

try:
    diccionario_paises=[]
    with open ('paises.csv', 'r', encoding="utf-8" ) as archivo:
        encabezado=next(archivo)
        for linea in archivo:
            linea_procesada=linea.strip().split(",")
            linea_paises={
                'nombre': linea_procesada[0],
                'poblacion': int(linea_procesada[1]),
                'superficie': int(linea_procesada[2]),
                'continente': quitar_acentos(linea_procesada[3])
                }
            diccionario_paises.append(linea_paises)

except FileNotFoundError:
    print("Error: no se encontró el archivo paises.csv.")
    exit()
except ValueError:
    print("Error: el archivo contiene datos invalidos.")
    exit()
except IndexError:
    print("Error: una linea del archivo tiene un formato incorrecto.")
    exit()



#Bloque 2: Lógica de las funcionalidades del menú

def funcionalidad_1(diccionario):
    pais_agregado=valida_nombre("Ingrese el nombre del país que desea agregar: ",diccionario)
    poblacion_agregada=numero_entero_positivo("Ingrese la población: ")
    superficie_agregada=numero_entero_positivo("Ingrese la superficie: ")
    continente_agregado=valida_continente("Ingrese a que continente pertenece: ")
    datos_agregados={
        'nombre': pais_agregado,
        'poblacion': poblacion_agregada,
        'superficie': superficie_agregada,
        'continente': continente_agregado
            }
    diccionario.append(datos_agregados)
    print("País agregado correctamente.")
    return

def funcionalidad_2(diccionario):
    #Usamos la función validadora "valida_continente" ya que esta admite repetidos
    pais_buscado=valida_continente("Ingrese el país a modificar: ")
    for pais in diccionario:
        if pais['nombre'] == pais_buscado:
            nueva_poblacion=numero_entero_positivo("Ingrese la nueva población: ")
            nueva_superficie=numero_entero_positivo("Ingrese la nueva superficie: ")
            pais['poblacion'] = nueva_poblacion
            pais['superficie'] = nueva_superficie
            print("Datos actualizados correctamente")
            return
    # Si el bucle principal termina sin return, el país ingresado no esta en el dataset.
    print("El país ingresado no se encuentra en la lista de países.")

def funcionalidad_3(diccionario):
    busqueda = valida_continente("Ingrese el nombre o parte del nombre a buscar: ")
    resultados = []
    for pais in diccionario:
        if busqueda.lower() in pais['nombre'].lower():
            resultados.append(pais)
    if len(resultados) == 0:
        print("No se encontraron países con ese nombre.")
    elif len(resultados) == 1:
        print("Se encontro 1 resultado:")
        print(f"Nombre: {resultados[0]['nombre']} | Población: {resultados[0]['poblacion']} | Superficie: {resultados[0]['superficie']} | Continente: {resultados[0]['continente']}")
    else:
        print(f"Se encontraron {len(resultados)} resultados:")    
        for pais in resultados:
            print(f"Nombre: {pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} | Continente: {pais['continente']}")

def guardar_csv(diccionario):
    with open('paises.csv', 'w', encoding='utf-8') as archivo:
        archivo.write('nombre,poblacion,superficie,continente\n')
        for pais in diccionario:
            archivo.write(f"{pais['nombre']},{pais['poblacion']},{pais['superficie']},{pais['continente']}\n")
    print("Datos guardados correctamente.")

#Bloque 3: Logica del menú

ingreso_menu = True

while ingreso_menu:
    print("Menu:")
    print("1- Agregar pais.")
    print("2- Actualizar poblacion y superficie.")
    print("3- Buscar pais por nombre.")
    print("4- Filtrar paises.")
    print("5- Ordenar paises.")
    print("6- Mostrar estadisticas.")
    print("7- Guardar y salir.")

    opcion = numero_entero_positivo("Ingrese opcion: ")

    match opcion:
        case 1:
            funcionalidad_1(diccionario_paises)
        case 2:
            funcionalidad_2(diccionario_paises)
        case 3:
            funcionalidad_3(diccionario_paises)
        case 4:
            print("Menu:")
            print("1- Filtrar por continente.")
            print("2- Filtrar por rango de poblacion.")
            print("3- Filtrar por rango de superficie.")

            opcion = numero_entero_positivo("Ingrese opcion: ")

            match opcion:
                case 1:
                    continente = quitar_acentos(input("Ingrese continente: "))
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
                            print(f"{pais['nombre']} - {pais['poblacion']}")
                case 3:
                    minimo = numero_entero_positivo("Ingrese superficie minima: ")
                    maximo = numero_entero_positivo("Ingrese superficie maxima: ")

                    resultado = filtrar_por_superficie(diccionario_paises, minimo, maximo)

                    if len(resultado) == 0:
                        print("No se encontraron paises en ese rango.")
                    else:
                        for pais in resultado:
                            print(f"{pais['nombre']} - {pais['superficie']}")
        case 5:
            print("Menu:")
            print("1- Ordenar paises por nombre.")
            print("2- Ordenar paises por poblacion.")
            print("3- Ordenar paises por superficie.")

            opcion = numero_entero_positivo("Ingrese opcion(1/3): ")

            match opcion:
                case 1:
                    print(f"{ordenar_paises(diccionario_paises)}")
                
                case 2:
                    print(f"{ordenar_por_poblacion(diccionario_paises)}")
                
                case 3:
                    print("Menu:")
                    print("1- Ordenar de forma ascendente")
                    print("2- Ordenar de forma descendiente")

                    opcion = numero_entero_positivo("Ingrese opcion: ")

                    match opcion:
                        case 1:
                            print(f"{superficie_menor_a_mayor(diccionario_paises)}")
                        case 2:
                            print(f"{superficie_mayor_a_menor(diccionario_paises)}")
        case 6:
            print("Menu:")
            print("1- Pais con mayor y menor poblacion.")
            print("2- Promedio de poblacion.")
            print("3- Promedio de superficie.")
            print("4- Cantidad de paises por continente")

            opcion = numero_entero_positivo("Ingrese opcion: ")

            match opcion:
                case 1:
                    print(f"{mayor_y_menor_poblacion(diccionario_paises)}")
                
                case 2:
                    print(f"{promedio_poblacion(diccionario_paises)}")
                
                case 3:
                    continente_promedio = promedio_superficie_continente(diccionario_paises, quitar_acentos(input("Ingrese continente: ")))

                    if continente_promedio is not None:
                        print(f"Promedio de superficie: {continente_promedio:.2f} km²")
                    else:
                        print(f"No se encontraron paises para ese continente.")
                case 4:
                    cantidad = (paises_en_continente(diccionario_paises, quitar_acentos(input("Ingrese continente: "))))

                    if cantidad == 0: 
                        print(f"no se encontraron países para ese continente")
                    else:
                        print(f"El continente tiene {cantidad} países.")

        case 7:
            guardar_csv(diccionario_paises)
            print("Saliendo....")
            ingreso_menu = False


