
from Nodo import ClaseNodo

class ClaseLista:

    
    def __init__(self):
        self.__cantNodo__ = 0
        self.__L__ = None

        
    def add(self, x):
        Ant = None
        p = self.__L__

        while p is not None and x >= p.getData():
            Ant = p
            p = p.getLink()

        nuevo = None
        if Ant is None:  # x es menor a todos los que están en la Lista (o __L__ es None)
            nuevo = ClaseNodo(x)
            nuevo.setLink(self.__L__)
            self.__L__ = nuevo
            self.__cantNodo__ += 1
        else:
            if Ant.getData() != x:  # x no está en la lista. Insertarlo entre Ant y p
                nuevo = ClaseNodo(x)
                Ant.setLink(nuevo)
                nuevo.setLink(p)
                self.__cantNodo__ += 1

    def length(self):
        return self.__cantNodo__
    
    def get(self,posicion):
        contador = 0
        aux = self.__L__
        while aux is not None:
            if contador == posicion:
                return aux.getData()
            aux = aux.getLink()
            contador += 1
        return -1
    
    def mostrar_lista(self):
        lista_nodos = []
        aux = self.__L__
        while aux is not None:
            lista_nodos.append(aux.getData())
            aux = aux.getLink()
        return lista_nodos
    
    
    
if __name__ == "__main__":
    l1 = ClaseLista()
    l1.add(5)
    l1.add(3)
    l1.add(10)
    l1.add(1)
    print(l1.mostrar_lista())
