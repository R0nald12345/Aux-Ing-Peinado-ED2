from ClaseNodoMvias import NodoMVias

class ArbolMViasBusqueda:
    def __init__(self, orden=3):
        """ Constructor de la clase ArbolMViasBusqueda. """
        if orden < 3:
            raise ValueError("El orden debe ser al menos 3.")
        self.raiz = None  # Inicializa la raíz del árbol como None
        self.orden = orden  # Establece el orden del árbol
        self.POSICION_INVALIDA = -1  # Valor para indicar posición no válida

    def vaciar(self):
        """ Vacía el árbol estableciendo la raíz como None. """
        self.raiz = None

    def es_arbol_vacio(self):
        """ Verifica si el árbol está vacío. """
        return self.raiz is None

    def insertar(self, numero):
        """ Inserta un número en el árbol. Si el árbol está vacío, crea un nuevo nodo raíz. """
        if self.es_arbol_vacio():
            self.raiz = NodoMVias(self.orden, numero)  # Crea la raíz con el número
        else:
            self._insertar_recursivo(self.raiz, numero)

    def _insertar_recursivo(self, nodo, numero):
        """ Inserta recursivamente un número en un nodo específico. """
        if nodo.es_hoja():
            if nodo.estan_numeros_llenos():
                # Necesita dividir y crear un nuevo nodo
                pos_bajar = self._get_posicion_por_donde_bajar(nodo, numero)
                if nodo.es_hijo_vacio(pos_bajar):
                    nodo.set_hijo(pos_bajar, NodoMVias(self.orden, numero))
                else:
                    self._insertar_recursivo(nodo.get_hijo(pos_bajar), numero)
            else:
                # Insertar número en el nodo
                self._insertar_numero_en_nodo(nodo, numero)
        else:
            # Si no es hoja, continuar bajando
            pos_bajar = self._get_posicion_por_donde_bajar(nodo, numero)
            if nodo.es_hijo_vacio(pos_bajar):
                nodo.set_hijo(pos_bajar, NodoMVias(self.orden, numero))
            else:
                self._insertar_recursivo(nodo.get_hijo(pos_bajar), numero)

    def _insertar_numero_en_nodo(self, nodo, numero):
        """ Inserta un número en un nodo, desplazando los existentes. """
        pos_insertar = self._get_posicion_donde_insertar(nodo, numero)
        # Desplazar números hacia la derecha
        for i in range(nodo.cantidad_de_numeros_no_vacios(), pos_insertar, -1):
            nodo.set_numero(i, nodo.get_numero(i - 1))
        nodo.set_numero(pos_insertar, numero)  # Asigna el nuevo número

    def _get_posicion_donde_insertar(self, nodo, numero):
        """ Obtiene la posición en la que se debe insertar un nuevo número. """
        for i in range(nodo.cantidad_de_numeros_no_vacios()):
            if numero < nodo.get_numero(i):
                return i
        return nodo.cantidad_de_numeros_no_vacios()  # Insertar al final

    def _get_posicion_por_donde_bajar(self, nodo, numero):
        """ Obtiene la posición del hijo por donde se debe bajar. """
        for i in range(nodo.cantidad_de_numeros_no_vacios()):
            if numero < nodo.get_numero(i):
                return i
        return nodo.cantidad_de_numeros_no_vacios()  # Bajar al final

    def recorrido_en_in_orden(self):
        """ Realiza un recorrido en in-orden y retorna una lista con los números. """
        recorrido = []
        self._recorrido_en_in_orden(self.raiz, recorrido)
        return recorrido

    def _recorrido_en_in_orden(self, nodo, recorrido):
        """ Método auxiliar para realizar el recorrido en in-orden. """
        if nodo is None:
            return
        for i in range(nodo.cantidad_de_numeros_no_vacios()):
            self._recorrido_en_in_orden(nodo.get_hijo(i), recorrido)
            recorrido.append(nodo.get_numero(i))
        self._recorrido_en_in_orden(nodo.get_hijo(nodo.cantidad_de_numeros_no_vacios()), recorrido)

    def altura(self):
        """ Calcula la altura del árbol. """
        return self._altura_recursivo(self.raiz)

    def _altura_recursivo(self, nodo):
        """ Calcula la altura de un nodo recursivamente. """
        if nodo is None:
            return 0
        if nodo.es_hoja():
            return 1
        # Calcula la altura máxima entre los hijos
        return 1 + max(self._altura_recursivo(hijo) for hijo in nodo.lista_de_hijos if hijo is not None)

