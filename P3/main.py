# from matriz import MatrizFloat
# from utils import leer_int, crear_menu

def main():
    opciones_principales = [
        "1. Construir matriz 1D",
        "2. Construir matriz 2D",
        "3. Construir matriz identidad",
        "4. Introducir matriz",
        "5. Mostrar matriz",
        "6. Operaciones con matrices",
        "7. Terminar"
    ]
    
    opciones_operaciones = [
        "1. Sumar matrices",
        "2. Restar matrices",
        "3. Volver al menú principal"
    ]
    
    # Bucle while para mantener el programa vivo usando crear_menu()
    while True:
        opcion = crear_menu(opciones_principales)
        
        if opcion == 1:
            n = leer_int("Número de elementos: ")
            matriz_actual.crear_matriz1D(n)
            
        elif opcion == 2:
            filas = leer_int("Número de filas: ")
            cols = leer_int("Número de columnas: ")
            matriz_actual.crear_matriz2D(filas, cols)
            
        elif opcion == 3:
            n = leer_int("Tamaño n de la matriz identidad: ")
            matriz_actual = MatrizFloat.matriz_identidad(n)
            
        elif opcion == 4:
            matriz_actual.introducir()
            
        elif opcion == 5:
            matriz_actual.mostrar()
            
        elif opcion == 6:
            # BUCLE DEL SUBMENÚ DE OPERACIONES
            while True:
                op_alg = crear_menu(opciones_operaciones)
                
                if op_alg == 1:
                    # Lógica para pedir segunda matriz y sumar
                    pass
                elif op_alg == 2:
                    # Lógica para pedir segunda matriz y restar
                    pass
                elif op_alg == 3:
                    # AQUÍ ESTÁ "VOLVER AL MENÚ PRINCIPAL"
                    break  # Sale del submenú y regresa al bucle principal
                    
        elif opcion == 7:
            print("Programa finalizado.")
            break  # Sale del bucle principal y termina el programa

if __name__ == "__main__":
    main()