from funciones import valida_nombre,valida_continente,numero_entero_positivo

#Bloque 1: Carga del Dataset y construcción del diccionario

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
    pass

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
    print("1- Agregar pais")
    print("2- Actualizar poblacion")
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
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass
        case 7:
            guardar_csv(diccionario_paises)
            print("Saliendo....")
            ingreso_menu = False
            break


