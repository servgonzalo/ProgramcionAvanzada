def leer_int(mensaje: str = "Introduce un número entero: ") -> int:
    """
    Función auxiliar que lee un número entero del teclado.
    Si se introduce un valor no válido, se solicita de nuevo.
    
    Parámetros:
        mensaje: El mensaje que se muestra al usuario solicitando la entrada (str).
                 Por defecto "Introduce un número entero: "

    Devuelve:
        int: El valor entero introducido por el usuario.
    """
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Error: Debes introducir un número entero válido.")


def leer_float(mensaje: str = "Introduce un número decimal: ") -> float:
    """
    Función auxiliar que solicita al usuario un número decimal.
    Si se introduce un valor no válido, se solicita de nuevo.
    
    Parámetros:
        mensaje: El mensaje que se muestra al usuario solicitando la entrada (str).
                 Por defecto "Introduce un número decimal: "
        
    Devuelve:
        float: El valor decimal introducido por el usuario.
    """
    while True:
        try:
            numerodec = float(input(mensaje))
            return numerodec
        except ValueError:
            print("Error: Debes introducir un número decimal válido.")


def crear_menu(opciones_menu: list) -> int:
    """
    Función que muestra un menú de opciones y solicita al usuario
    que seleccione una opción válida.
    
    Parámetros:
        opciones_menu: lista de opciones a mostrar en el menú (list)
                      
    Devuelve:
        int: El número de opción seleccionado por el usuario.
    """
    print("\nElige una de las opciones del menú:")
    print("Menú:")
    
    # Recorremos la lista de opciones recibida como parámetro
    for opcion in opciones_menu:
        print(opcion)
        
    # Validamos que el usuario elija un número dentro del rango de la lista
    while True:
        opcion_seleccionada = leer_int("Selecciona una opción: ")
        if 1 <= opcion_seleccionada <= len(opciones_menu):
            return opcion_seleccionada
        else:
            print(f"Error: Por favor, selecciona un número entre 1 y {len(opciones_menu)}.")