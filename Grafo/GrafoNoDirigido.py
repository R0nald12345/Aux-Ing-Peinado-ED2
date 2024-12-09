from collections import deque  # Importar deque para usar como cola en BFS

class Grafo:
    # Constructor: Inicializa el grafo con una lista de adyacencia vacía y un contador de aristas
    def __init__(self, nro_de_vertice_inicial=0):
        if nro_de_vertice_inicial < 0:
            raise ValueError("Error: número de vértices inicial no válido")
        self.lista_de_adyacencia = []  # Lista de adyacencia para almacenar las conexiones
        self.cant_aristas = 0  # Contador de aristas
        self.vectorMarcado = []  # Vector para marcar los nodos visitados (se inicializa dinámicamente)
        
        # Inicializa la lista de adyacencia con listas vacías para cada vértice
        for _ in range(nro_de_vertice_inicial):
            self.lista_de_adyacencia.append([])
    
    # Método para insertar un nuevo vértice
    def insertar_vertice(self):
        self.lista_de_adyacencia.append([])  # Añadir una nueva lista vacía
        self.vectorMarcado.append(False)  # Inicializar como no visitado
    
    # Método para obtener la cantidad de aristas
    def cantidad_aristas(self):
        return self.cant_aristas
    
    # Método para obtener la cantidad de vértices
    def cantidad_vertices(self):
        return len(self.lista_de_adyacencia)
    
    # Validar si un vértice es válido
    def validar_vertice(self, posicion_vertice):
        if posicion_vertice < 0 or posicion_vertice >= self.cantidad_vertices():
            raise ValueError("Error: número de vértice no válido")
    
    # Insertar una arista entre dos vértices
    def insertar_arista(self, pos_vertice_origen, pos_vertice_destino):
        self.validar_vertice(pos_vertice_origen)  # Validar el vértice de origen
        self.validar_vertice(pos_vertice_destino)  # Validar el vértice de destino
        if self.existe_adyacencia(pos_vertice_origen, pos_vertice_destino):
            raise ValueError("Ya existe adyacencia")  # Verificar duplicados
        self.cant_aristas += 1  # Incrementar el contador de aristas
        # Añadir la conexión en ambas direcciones (grafo no dirigido)
        self.lista_de_adyacencia[pos_vertice_origen].append(pos_vertice_destino)
        self.lista_de_adyacencia[pos_vertice_destino].append(pos_vertice_origen)
    
    # Verificar si existe una conexión entre dos vértices
    def existe_adyacencia(self, pos_vertice_origen, pos_vertice_destino):
        self.validar_vertice(pos_vertice_origen)
        self.validar_vertice(pos_vertice_destino)
        adyacencia_del_origen = self.lista_de_adyacencia[pos_vertice_origen]
        return pos_vertice_destino in adyacencia_del_origen

    # Mostrar el grafo (para grafo no dirigido)
    def mostrar_grafo_no_dirigido(self):
        for i in range(len(self.lista_de_adyacencia)):
            vertice = f"[{i}]"  # Representar el vértice actual
            adyacentes = "["  # Construir la lista de adyacencias
            for j in self.lista_de_adyacencia[i]:
                adyacentes += f"{j},"
            if self.lista_de_adyacencia[i]:
                adyacentes = adyacentes[:-1]  # Eliminar la última coma
            adyacentes += "]"
            print(f"{vertice} -> {adyacentes}")
    
    # Desmarcar todos los vértices (para reiniciar las búsquedas)
    def desmarcarTodos(self):
        self.vectorMarcado = [False] * self.cantidad_vertices()

    # Marcar un vértice como visitado
    def marcar(self, u):
        self.vectorMarcado[u] = True

    # Verificar si un vértice ya está marcado
    def isMarcado(self, u):
        return self.vectorMarcado[u]

    # DFS iterativo utilizando una pila
    def DFS(self, start):
        self.desmarcarTodos()  # Desmarcar todos los vértices
        stack = [start]  # Inicializar la pila con el vértice inicial
        while stack:  # Mientras la pila no esté vacía
            current = stack.pop()  # Obtener el vértice actual
            if not self.isMarcado(current):  # Si el vértice no ha sido visitado
                self.marcar(current)  # Marcar el vértice como visitado
                print(current, end=' ')  # Imprimir el vértice visitado
                # Agregar los vértices adyacentes no marcados a la pila
                for neighbor in reversed(self.lista_de_adyacencia[current]):  # Revertimos para mantener orden
                    if not self.isMarcado(neighbor):
                        stack.append(neighbor)


    # BFS iterativo utilizando una cola
    def BFS(self, start):
        self.desmarcarTodos()  # Desmarcar todos los vértices
        queue = deque([start])  # Inicializar la cola con el vértice inicial
        while queue:  # Mientras la cola no esté vacía
            current = queue.popleft()  # Obtener el vértice actual
            if not self.isMarcado(current):  # Si el vértice no ha sido visitado
                self.marcar(current)  # Marcar el vértice como visitado
                print(current, end=' ')  # Imprimir el vértice visitado
                # Agregar los vértices adyacentes no marcados a la cola
                for neighbor in self.lista_de_adyacencia[current]:
                    if not self.isMarcado(neighbor):
                        queue.append(neighbor)


# Ejemplo de uso
if __name__ == "__main__":
    grafo_no_dirigido = Grafo()
    
    # Agregar vértices
    for _ in range(9):
        grafo_no_dirigido.insertar_vertice()
    
    # Agregar aristas
    # Agregar aristas
    grafo_no_dirigido.insertar_arista(0, 1)
    grafo_no_dirigido.insertar_arista(0, 5)

    # No es necesario agregar la arista (1, 0) porque ya se agregó (0, 1)

    grafo_no_dirigido.insertar_arista(2, 3)
    grafo_no_dirigido.insertar_arista(2, 4)
    grafo_no_dirigido.insertar_arista(2, 5)
    grafo_no_dirigido.insertar_arista(2, 6)
    grafo_no_dirigido.insertar_arista(2, 7)

    # No es necesario agregar la arista (3, 2) porque ya se agregó (2, 3)
    grafo_no_dirigido.insertar_arista(3, 4)
    grafo_no_dirigido.insertar_arista(3, 8)

    # No es necesario agregar la arista (4, 2) porque ya se agregó (2, 4)
    # No es necesario agregar la arista (4, 3) porque ya se agregó (3, 4)

    # No es necesario agregar la arista (5, 0) porque ya se agregó (0, 5)
    # No es necesario agregar la arista (5, 2) porque ya se agregó (2, 5)

    # No es necesario agregar la arista (6, 2) porque ya se agregó (2, 6)

    # No es necesario agregar la arista (7, 2) porque ya se agregó (2, 7)
    grafo_no_dirigido.insertar_arista(7, 8)

    # No es necesario agregar la arista (8, 3) porque ya se agregó (3, 8)
    # No es necesario agregar la arista (8, 7) porque ya se agregó (7, 8)
    
    # Mostrar el grafo
    grafo_no_dirigido.mostrar_grafo_no_dirigido()
    
    print("\nDFS desde el vértice 0:")
    grafo_no_dirigido.DFS(0)  # Realizar DFS desde el vértice 0
    
    print("\n\nBFS desde el vértice 0:")
    grafo_no_dirigido.BFS(0)  # Realizar BFS desde el vértice 0
