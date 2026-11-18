import numpy as np
from utils import leer_float  # Reutilizamos la función auxiliar de utils.py

class MatrizFloat:
    """
    Clase que representa una matriz dinámica 1D/2D.
    
    Atributos de clase:
        TIPO_DATO # Tipo de dato por defecto (np.float32)
        
    Atributos de instancia (protegidos):
        _matriz   # Almacena la matriz (utilice numpy)
        _nfil     # Almacena número de filas de la matriz (int)
        _ncol     # Almacena número de columnas de la matriz (int)
    """
    
    TIPO_DATO = np.float32

    def __init__(self):
        """
        Inicializador. No recibe parámetros adicionales.
        Inicializa el atributo matriz con None y los atributos
        nfil y ncol a 0
        """
        self._matriz = None
        self._nfil = 0
        self._ncol = 0

    @classmethod
    def matriz_identidad(cls, n: int):
        """
        Método de clase que crea y devuelve una nueva
        instancia de MatrizFloat configurada como matriz
        identidad de tamaño n x n
        
        Parámetros:
            n: El tamaño n de la matriz
            
        Devuelve:
            Nueva instancia con matriz identidad creada
            (MatrizFloat)
        """
        nueva_instancia = cls()
        nueva_instancia._matriz = np.eye(n, dtype=cls.TIPO_DATO)
        nueva_instancia._nfil = n
        nueva_instancia._ncol = n
        return nueva_instancia

    def mismas_dimensiones(self, m1, m2) -> bool:
        """
        Método para comparar dimensiones.
        
        Parámetros:
            m1: Primera matriz a comparar (MatrizFloat)
            m2: Segunda matriz a comparar (MatrizFloat)
            
        Devuelve:
            bool: True si ambas matrices tienen el mismo número de
            filas y columnas, y False en caso contrario
            (o si alguna no está creada)
        """
        if not m1.existe() or not m2.existe():
            return False
        return (m1._nfil == m2._nfil) and (m1._ncol == m2._ncol)

    def crear_matriz2D(self, nFil: int, nCol: int):
        """
        Método para crear una matriz bidimensional de ceros.
        Asigna valores de filas y columnas según parámetros.
        
        Parámetros:
            nFil: Número de filas (int)
            nCol: Número de columnas (int)
        """
        self._nfil = nFil
        self._ncol = nCol
        self._matriz = np.zeros((nFil, nCol), dtype=self.TIPO_DATO)

    def crear_matriz1D(self, nElementos: int):
        """
        Método para crear una matriz unidimensional de ceros.
        Usa crear_matriz2D para asignar 1 fila y n columnas.
        
        Parámetros:
            nElementos: Número de elementos de la fila (int)
        """
        self.crear_matriz2D(1, nElementos)

    def existe(self) -> bool:
        """
        Método que verifica si matriz está creada y no está vacía
        
        Devuelve:
            True si existe, de lo contrario False
        """
        return self._matriz is not None and self._matriz.size > 0

    def introducir(self):
        """
        Método que solicita por consola el valor numérico decimal
        para cada posición (i, j) de la matriz.
        Da error si se intenta introducir datos sin haber creado la
        matriz previamente.
        """
        if not self.existe():
            print("Error: La matriz no ha sido creada todavía.")
            return

        for i in range(self._nfil):
            for j in range(self._ncol):
                valor = leer_float(f"Introduce el valor para la posición ({i}, {j}): ")
                self._matriz[i, j] = valor

    def mostrar(self):
        """
        Método para mostrar las dimensiones y los elementos de la
        matriz. Si la matriz no existe (existe() == False), muestra
        un mensaje advirtiéndolo
        """
        if not self.existe():
            print("Advertencia: La matriz no existe o está vacía.")
            return

        print(f"Dimensiones: {self._nfil} x {self._ncol}")
        print(self._matriz)

    # ===========================================================
    # OPERACIONES ALGEBRAICAS
    # ===========================================================

    def sumar_matrices(self, otra_matriz):
        """
        Método que suma la matriz actual con otra matriz.
        
        Parámetros:
            otra_matriz: objeto de MatrizFloat con la matriz a sumar
            
        Devuelve:
            Un nuevo objeto MatrizFloat con la matriz resultante de
            la suma (o None si no tienen las mismas dimensiones).
        """
        if not self.mismas_dimensiones(self, otra_matriz):
            print("Error: Las matrices no existen o no tienen las mismas dimensiones.")
            return None

        resultado = MatrizFloat()
        resultado._nfil = self._nfil
        resultado._ncol = self._ncol
        resultado._matriz = self._matriz + otra_matriz._matriz
        return resultado

    def restar_matrices(self, otra_matriz):
        """
        Método que resta la matriz actual con otra matriz.
        
        Parámetros:
            otra_matriz: objeto de MatrizFloat con la matriz a restar
            
        Devuelve:
            Un nuevo objeto MatrizFloat con la matriz resultante de
            la resta (o None si no tienen las mismas dimensiones).
        """
        if not self.mismas_dimensiones(self, otra_matriz):
            print("Error: Las matrices no existen o no tienen las mismas dimensiones.")
            return None

        resultado = MatrizFloat()
        resultado._nfil = self._nfil
        resultado._ncol = self._ncol
        resultado._matriz = self._matriz - otra_matriz._matriz
        return resultado