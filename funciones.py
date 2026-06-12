
def valida_continente(mensaje):
    """
    Solicita y valida una entrada de texto genérica (usada para continentes o búsquedas).
    Verifica que la cadena no esté vacía y no esté compuesta únicamente por números.
    """
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
    """
    Solicita un número al usuario y asegura que sea un entero estrictamente positivo.
    Atrapa errores de tipeo (letras) y valores negativos o cero.
    """
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
    """
    Solicita y valida el nombre de un país nuevo.
    Aplica las reglas de texto genéricas y además verifica que no existan duplicados en memoria.
    """
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
            # Regla 3: No puede estar duplicado en nuestra lista (lista de diccionarios)
            for item in diccionario:
                if item['nombre'] == nombre:
                    raise ValueError(f"El país '{nombre}' ya se encuentra en el diccionario.")
            # Si sobrevivió a todas las validaciones, lo retornamos
            return nombre
        except ValueError as e:
            print(f"ERROR: {e}")

def filtrar_por_continente(paises, continente):
    """
    Retorna una lista de países que pertenecen a un continente específico.
    La comparación se hace en minúsculas para evitar problemas de "Case Sensitivity".
    """
    resultado = []

    for pais in paises:
        if pais ["continente"].lower() == continente.lower():
            resultado.append(pais)
    
    return resultado

def filtrar_por_rango_poblacion(paises, minimo, maximo):
    """Filtra y retorna los países cuya población se encuentre dentro de un rango numérico."""
    resultado = []
    resultado = []

    for pais in paises:
        if minimo <= pais["poblacion"]<= maximo:
            resultado.append(pais)

    return resultado

def filtrar_por_superficie(paises, minimo, maximo):
    """Filtra y retorna los países cuya superficie se encuentre dentro de un rango numérico."""
    resultado = []
    for pais in paises:
        if minimo <= pais["superficie"] <= maximo:
            resultado.append(pais)

    for pais in paises:
        if minimo <= pais["superficie"] <= maximo:
            resultado.append(pais)

    return resultado

def ordenar_paises(paises):
    """Ordena alfabéticamente los países por nombre e imprime el resultado."""
    paises_ordenados = sorted(paises, key=lambda pais: pais["nombre"])
    
    for pais in paises_ordenados:
        print(pais["nombre"])

def ordenar_por_poblacion(paises):
    """Ordena los países de menor a mayor población e imprime el resultado con formato."""
    paises_ordenados = sorted(paises, key=lambda pais: pais['poblacion'])

    for pais in paises_ordenados:
        print(f"{pais['nombre']}: {pais['poblacion']:,} habitantes.".replace(",", "."))

def superficie_menor_a_mayor(paises):
    """Ordena los países por superficie en forma ascendente."""
    paises_ordenados = sorted(paises, key=lambda pais: pais["superficie"])

    for pais in paises_ordenados:
        print(f"{pais["nombre"]}: {pais["superficie"]:,} km² de superficie.")

def superficie_mayor_a_menor(paises):
    """Ordena los países por superficie en forma descendente usando reversed()."""
    paises_ordenados = reversed(sorted(paises, key=lambda pais: pais["superficie"]))

    for pais in paises_ordenados:
        print(f"{pais["nombre"]}: {pais["superficie"]:,} km² de superficie.")

def mayor_y_menor_poblacion(paises):
    """Busca y muestra el país con más habitantes y el país con menos habitantes."""
    pais_mas_poblado = max(paises, key=lambda pais: pais["poblacion"])
    pais_menos_poblado = min(paises, key=lambda pais: pais["poblacion"])
    
    print (f"Pais mas poblado: {pais_mas_poblado['nombre']} {pais_mas_poblado['poblacion']:,} habitantes.".replace(",", "."))
    print (f"Pais menos poblado: {pais_menos_poblado['nombre']} {pais_menos_poblado['poblacion']:,} habitantes".replace(",","."))

def promedio_poblacion(paises):
    """Calcula y muestra la densidad poblacional (habitantes por km²) de cada país."""
    for pais in paises:
        densidad = pais['poblacion'] / pais['superficie']

        print(f"{pais['nombre']}: {densidad:.2f} hab/km²")

def promedio_superficie_continente(paises, continente):
    """Calcula el promedio matemático de la superficie de los países de un continente dado."""
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
    """
    Elimina las tildes y caracteres diacríticos de un texto.
    Útil para normalizar las búsquedas y evitar errores de comparación.
    """
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn')

def paises_en_continente(paises, continente):
    """Cuenta cuántos países registrados hay en un continente especificado."""
    contador = 0
    
    for pais in paises:
        if pais['continente'].lower() == continente.lower():
            contador += 1
    
    return contador