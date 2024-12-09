from ListaSimple import Lista

from collections import deque

class Grafo:
    MAXVERTEX = 49

    def __init__(self):
        self.V = [Lista() for _ in range(self.MAXVERTEX + 1)]
        self.n = -1
        self.marca = [False for _ in range(self.MAXVERTEX + 1)]

    def add_vertice(self):
        if self.n == self.MAXVERTEX:
            print("Grafo.addVertice: Demasiados vértices (solo se permiten {})".format(self.MAXVERTEX + 1))
            return
        self.n += 1
        self.V[self.n] = Lista()

    def cant_vertices(self):
        return self.n + 1

    def is_vertice_valido(self, v, metodo=None):
        valido = 0 <= v <= self.n
        if not valido and metodo is not None:
            print("Grafo.{}: {} no es un vértice del Grafo {}".format(metodo, v, self.get_indicacion()))
        return valido

    def add_arista(self, u, peso, v):
        if peso <= 0:
            print("Grafo.addArista: El peso debe ser mayor que cero")
            return
        if not self.is_vertice_valido(u, "addArista") or not self.is_vertice_valido(v, "addArista"):
            return
        self.V[u].add(v, peso)

    def del_arista(self, u, v):
        if not self.is_vertice_valido(u, "delArista") or not self.is_vertice_valido(v, "delArista"):
            return
        self.V[u].del_data(v)

    def costo(self, u, v):
        if not self.is_vertice_valido(u) or not self.is_vertice_valido(v):
            return 0
        return self.V[u].get_peso(v)

    def dfs(self, v):
        if not self.is_vertice_valido(v, "dfs"):
            return
        self.desmarcar_todos()
        print("DFS:", end="")
        self.dfs1(v)
        print()

    def dfs1(self, v):
        print(" {}".format(v), end="")
        self.marcar(v)
        for i in range(self.V[v].length()):
            w = self.V[v].get(i)
            if not self.is_marcado(w):
                self.dfs1(w)

    def bfs(self, u):
        if not self.is_vertice_valido(u, "bfs"):
            return
        self.desmarcar_todos()
        cola = [u]
        self.marcar(u)
        print("BFS:", end="")
        while cola:
            v = cola.pop(0)
            print(" {}".format(v), end="")
            for i in range(self.V[v].length()):
                w = self.V[v].get(i)
                if not self.is_marcado(w):
                    cola.append(w)
                    self.marcar(w)
        print()


    def print_listas(self):
        if self.cant_vertices() == 0:
            print("(Grafo Vacío)")
        else:
            for i in range(self.n + 1):
                print("V[{}]-->{}".format(i, self.V[i]))


    def __str__(self):
        if self.cant_vertices() == 0:
            return "(Grafo Vacío)"
        self.desmarcar_todos()
        s = "["
        coma = ""
        for i in range(self.n + 1):
            for k in range(self.n + 1):
                peso = self.costo(i, k)
                if peso > 0:
                    arista = "({}, {}, {})".format(i, peso, k)
                    s += coma + arista
                    coma = ", "
                    self.marcar(i)
            if not self.is_marcado(i):
                s += coma + str(i)
                coma = ", "
        return s + "]"

    def desmarcar_todos(self):
        for i in range(self.n + 1):
            self.marca[i] = False

    def marcar(self, u):
        if self.is_vertice_valido(u):
            self.marca[u] = True

    def desmarcar(self, u):
        if self.is_vertice_valido(u):
            self.marca[u] = False

    def is_marcado(self, u):
        return self.marca[u]

    def obtener_menor_no_marcado(self, peso):
        i = 0
        while self.is_marcado(i):
            i += 1
        menor = peso[i]
        posicion = i
        for j in range(i + 1, len(peso)):
            if not self.is_marcado(j) and peso[j] < menor:
                menor = peso[j]
                posicion = j
        return posicion


    def shortest_path(self, a, z):
        peso = [float('inf')] * (self.n + 1)
        peso[a] = 0
        self.desmarcar_todos()
        while not self.is_marcado(z):
            u = self.obtener_menor_no_marcado(peso)
            self.marcar(u)
            for i in range(self.V[u].length()): #Adyacentes
                w = self.V[u].get(i)
                if not self.is_marcado(w):
                    s = peso[u] + self.costo(u, w)
                    if peso[w] > s:
                        peso[w] = s
        return peso[z]



    def floyd_warshall(self):
        # Inicializar la matriz de distancias con valores infinitos
        dist = [[float('inf')] * (self.n + 1) for _ in range(self.n + 1)]

        # Llenar la diagonal con 0, ya que la distancia de un vértice a sí mismo es 0
        for i in range(self.n + 1):
            dist[i][i] = 0

        # Llenar la matriz de adyacencia con los pesos actuales
        for u in range(self.n + 1):
            for i in range(self.V[u].length()):
                v = self.V[u].get(i)
                peso_uv = self.V[u].get_peso(v)
                dist[u][v] = peso_uv

        # Algoritmo de Floyd-Warshall para encontrar los caminos más cortos entre todos los pares
        for k in range(self.n + 1):
            for i in range(self.n + 1):
                for j in range(self.n + 1):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        

        # Mostrar la matriz de distancias mínimas entre todos los pares de vértices
        print("Matriz de distancias mínimas (Floyd-Warshall):")
        for i in range(self.n + 1):
            for j in range(self.n + 1):
                if dist[i][j] == float('inf'):
                    print("INF", end=" ")
                else:
                    print(dist[i][j], end=" ")
            print()

        return dist
   
if __name__ == "__main__":
    G = Grafo()
    G.add_vertice()
    G.add_vertice()
    G.add_vertice()
    G.add_vertice()
    G.add_vertice()
    # G.add_arista(1, 40, 2)
    # G.add_arista(1, 60, 3)
    # print("G={}".format(G))

    # ---------------------------------------------
    # G.add_arista(1, 100, 0)
    # G.add_arista(1, 10, 3)
    
    # G.add_arista(2, 5, 1)
    # G.add_arista(2, 80, 3)
    # G.add_arista(2, 150, 0)
    
    # G.add_arista(3, 15, 0)
    
    G.add_arista(0, 2, 1)
    G.add_arista(0, 1, 2)
    G.add_arista(0, 3, 4)
    
    G.add_arista(1, 4, 3)
    
    G.add_arista(2, 1, 1)
    G.add_arista(2, 1, 4)
    
    G.add_arista(3, 1, 0);
    G.add_arista(3, 3, 2)
    G.add_arista(3, 5, 4)
    
    
    G.print_listas()
    
    print(G.shortest_path(2, 0))
    #print(G.floyd_warshall())