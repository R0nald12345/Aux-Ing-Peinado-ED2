class NodoMVias:
    def __init__(self, orden, primer_numero=None):
        """
        Constructor de la clase NodoMVias.
        
        Parámetros:
        - orden: El orden del árbol M-Vías (número máximo de hijos por nodo).
        - primer_numero: (Opcional) El primer número a insertar en el nodo.
        """
        # Un nodo de orden M puede tener hasta (M-1) números.
        self.lista_de_numeros = [None] * (orden - 1)
        
        # Inicializa la lista de hijos con 'None'. El tamaño es 'orden' ya que
        # un nodo de orden M puede tener hasta M hijos.
        self.lista_de_hijos = [None] * orden
        
        # Si se proporciona un número inicial, lo asigna al primer índice.
        if primer_numero is not None:
            self.lista_de_numeros[0] = primer_numero

    @staticmethod
    def nodo_vacio():
        """ Método estático que representa un nodo vacío. """
        return None

    def get_numero(self, posicion):
        """ Obtiene el número en una posición específica. """
        return self.lista_de_numeros[posicion]

    def set_numero(self, posicion, numero):
        """ Asigna un número en una posición específica. """
        self.lista_de_numeros[posicion] = numero

    def get_hijo(self, posicion):
        """ Obtiene el hijo en una posición específica. """
        return self.lista_de_hijos[posicion]

    def set_hijo(self, posicion, nodo):
        """ Asigna un nodo hijo en una posición específica. """
        self.lista_de_hijos[posicion] = nodo

    def es_numero_vacio(self, posicion):
        """ Verifica si el número en una posición específica está vacío (None). """
        return self.lista_de_numeros[posicion] is None

    def es_hijo_vacio(self, posicion):
        """ Verifica si el hijo en una posición específica está vacío (None). """
        return self.lista_de_hijos[posicion] is None

    def es_hoja(self):
        """ Determina si el nodo es una hoja, es decir, si no tiene hijos. """
        return all(hijo is None for hijo in self.lista_de_hijos)

    def estan_numeros_llenos(self):
        """ Verifica si todas las posiciones de números en el nodo están ocupadas. """
        return all(numero is not None for numero in self.lista_de_numeros)

    def cantidad_de_hijos_no_vacios(self):
        """ Cuenta la cantidad de hijos que no están vacíos en el nodo. """
        return sum(1 for hijo in self.lista_de_hijos if hijo is not None)

    def cantidad_de_numeros_no_vacios(self):
        """ Cuenta la cantidad de números que no están vacíos en el nodo. """
        return sum(1 for numero in self.lista_de_numeros if numero is not None)

    def sumar_numeros_nodo(self):
        """ Suma todos los números presentes en el nodo. """
        return sum(numero for numero in self.lista_de_numeros if numero is not None)

    def verificar_existe_numero_en_nodo(self, numero):
        """ Verifica si un número específico existe en las listas de números del nodo. """
        return numero in self.lista_de_numeros
