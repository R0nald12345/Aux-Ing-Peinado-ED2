from Nodo import Nodo

class Lista:
    def __init__(self):
        self.L = None
        self.n = 0

    def add(self, data, peso):
        Ant = None
        p = self.L

        while p is not None and data >= p.get_data():
            Ant = p
            p = p.get_link()

        if Ant is None:  # data es menor a todos los que están en la Lista (o L==null)
            nuevo = Nodo(data, peso)
            nuevo.set_link(self.L)
            self.L = nuevo
            self.n += 1
        elif Ant.get_data() != data:  # data no está en la lista. Insertarlo entre Ant y p
            nuevo = Nodo(data, peso)
            Ant.set_link(nuevo)
            nuevo.set_link(p)
            self.n += 1

    def del_data(self, data):  # Elimina el nodo con Data=data, si existe.
        Ant = None
        p = self.L

        while p is not None and data > p.get_data():
            Ant = p
            p = p.get_link()

        if p is not None and p.get_data() == data:  # data existe en la Lista
            if Ant is None:
                self.L = self.L.get_link()  # data era el primero de la Lista
            else:
                Ant.set_link(p.get_link())

            p.set_link(None)
            self.n -= 1

    def existe(self, data):  # Devuelve true si el data especificado está en la lista.
        return self.exist(data) is not None

    def get(self, k):  # Devuelve el k-ésimo elemento de la lista k=0, 1, ..., length()-1
        p = self.L
        i = 0
        while p is not None:
            if i == k:
                return p.get_data()

            p = p.get_link()
            i += 1

        print("Lista.get: Fuera de rango")
        return -1

    def get_peso(self, data):  # Devuelve el Peso que acompaña al data. Si data no existe, devuelve 0.
        p = self.exist(data)
        if p is not None:
            return p.get_peso()

        return 0

    def length(self):
        return self.n

    def __str__(self):
        S = "["
        coma = ""

        p = self.L
        while p is not None:
            S += f"{coma}{p.get_data()}/{self.double_to_str(p.get_peso())}"
            coma = ", "
            p = p.get_link()

        return S + "]"

    def double_to_str(self, d):  # Devuelve d sin el punto decimal innecesario.
        s = str(d)
        pos_punto = s.find('.')
        for i in range(pos_punto + 1, len(s)):  # Ver si después del '.' todos son ceros.
            if s[i] != '0':
                return s

        return s[:pos_punto]

    def exist(self, data):  # Devuelve el puntero al Nodo donde se encuentra data.
        p = self.L

        while p is not None and data > p.get_data():
            p = p.get_link()

        if p is not None and p.get_data() == data:
            return p

        return None  # Devolver None, si data no existe en la lista.