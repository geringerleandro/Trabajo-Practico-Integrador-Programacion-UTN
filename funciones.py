
def valida_continente(mensaje):
    while True:
        try:
            # Pedimos el input, le sacamos espacios extra y lo ponemos en Title Case
            nombre = input(mensaje).strip().title()
            # Regla 1: No puede estar vacío
            if nombre == "":
                raise ValueError("El nombre no puede estar vacío.")
            # Regla 2: No puede ser únicamente números
            if nombre.isdigit():
                raise ValueError("El nombre no puede estar compuesto únicamente por números.")
            # Si sobrevivió a todas las validaciones, lo retornamos
            return nombre
        except ValueError as e:
            print(f"ERROR: {e}")

def numero_entero_positivo(mensaje):
    while True:
        try:
            # 1. Pedimos el dato
            ingreso = input(mensaje)
            # 2. Intentamos convertirlo a entero (lanza ValueError si tiene letras)
            numero = int(ingreso) 
            # 3. Debe ser estrictamente positivo
            if numero <= 0:
                raise ValueError("El número debe ser mayor a 0.")
            # 4. Si supera las validaciones, cortamos el bucle retornando el valor
            return numero
        except ValueError as e:
            # Atrapa tanto el error de int() como el de nuestro raise
            print(f"ERROR: Entrada inválida. {e} Intente nuevamente.")


def valida_nombre(mensaje, diccionario):
    while True:
        try:
            # Pedimos el input, le sacamos espacios extra y lo ponemos en Title Case
            nombre = input(mensaje).strip().title()

            #Regla 1: No puede estar vacío,
            if nombre == "":
                raise ValueError("El nombre no puede estar vacío.")
            # Regla 2: No puede ser únicamente números
            if nombre.isdigit():
                raise ValueError("El nombre no puede estar compuesto únicamente por números.")
            # Regla 3: No puede estar duplicado en nuestro inventario (lista de diccionarios)
            for item in diccionario:
                if item['nombre'] == nombre:
                    raise ValueError(f"El nombre '{nombre}' ya se encuentra en el diccionario.")
            # Si sobrevivió a todas las validaciones, lo retornamos
            return nombre
        except ValueError as e:
            print(f"ERROR: {e}")

def filtrar_por_continente(paises, continente):
    resultado = []

    for pais in paises:
        if pais ["continente"].lower() == continente.lower():
            resultado.append(pais)
    
    return resultado

def filtrar_por_rango_poblacion(paises, minimo, maximo):
    resultado = []

    for pais in paises:
        if minimo <= pais["poblacion"]<= maximo:
            resultado.append(pais)

    return resultado

def filtrar_por_superficie(paises, minimo, maximo):
    resultado = []

    for pais in paises:
        if minimo <= pais["superficie"] <= maximo:
            resultado.append(pais)

    return resultado

def ordenar_paises(paises):
    
    paises_ordenados = sorted(paises, key=lambda pais: pais["nombre"])
    
    for pais in paises_ordenados:
        print(pais["nombre"])

def ordenar_por_poblacion(paises):
    
    paises_ordenados = sorted(paises, key=lambda pais: pais['poblacion'])

    for pais in paises_ordenados:
        print(f"{pais['nombre']}: {pais['poblacion']:,} habitantes.".replace(",", "."))

def superficie_menor_a_mayor(paises):
    
    paises_ordenados = sorted(paises, key=lambda pais: pais["superficie"])

    for pais in paises_ordenados:
        print(f"{pais["nombre"]}: {pais["superficie"]:,} km² de superficie.")

def superficie_mayor_a_menor(paises):
    
    paises_ordenados = reversed(sorted(paises, key=lambda pais: pais["superficie"]))

    for pais in paises_ordenados:
        print(f"{pais["nombre"]}: {pais["superficie"]:,} km² de superficie.")

def mayor_y_menor_poblacion(paises):
    pais_mas_poblado = max(paises, key=lambda pais: pais["poblacion"])
    pais_menos_poblado = min(paises, key=lambda pais: pais["poblacion"])
    
    print (f"Pais mas poblado: {pais_mas_poblado['nombre']} {pais_mas_poblado['poblacion']:,} habitantes.".replace(",", "."))
    print (f"Pais menos poblado: {pais_menos_poblado['nombre']} {pais_menos_poblado['poblacion']:,} habitantes".replace(",","."))

def promedio_poblacion(paises):

    for pais in paises:
        densidad = pais['poblacion'] / pais['superficie']

        print(f"{pais['nombre']}: {densidad:.2f} hab/km²")

def promedio_superficie_continente(paises, continente):

    suma_superficie = 0
    cantidad_paises = 0

    for pais in paises:
        if pais['continente'].lower() == continente.lower():
            suma_superficie += pais['superficie']
            cantidad_paises += 1
    
    if cantidad_paises == 0:
        return None
    
    return suma_superficie/cantidad_paises

import unicodedata

def quitar_acentos(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn')

def paises_en_continente(paises, continente):
    contador = 0
    
    for pais in paises:
        if pais['continente'].lower() == continente.lower():
            contador += 1
    
    return contador