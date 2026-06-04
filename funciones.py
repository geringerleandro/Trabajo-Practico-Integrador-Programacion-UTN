
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

def numero_entero_positivo(numero):
    while True:
        try:
            # 1. Pedimos el dato
            ingreso = input(numero)
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

