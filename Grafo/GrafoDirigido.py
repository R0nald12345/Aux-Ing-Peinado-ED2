class GrafoDirigido:
    
    # Constructor: Inicializa el grafo con una lista de adyacencia vacía y una cantidad de aristas
    def __init__(self, nro_de_vertice_inicial=0):
        if nro_de_vertice_inicial < 0:
            raise ValueError("Error: número de vértices inicial no válido")
        self.lista_de_adyacencia = []  # Lista de adyacencia para almacenar conexiones
        self.cant_aristas = 0  # Contador de aristas
        for _ in range(nro_de_vertice_inicial):
            self.lista_de_adyacencia.append([])
    
    # Agregar un nuevo vértice al grafo
    def insertar_vertice(self):
        self.lista_de_adyacencia.append([])
    
    # Obtener la cantidad de aristas
    def cantidad_aristas(self):
        return self.cant_aristas
    
    # Obtener la cantidad de vértices
    def cantidad_vertices(self):
        return len(self.lista_de_adyacencia)
    
    # Validar que el índice del vértice sea válido
    def validar_vertice(self, posicion_vertice):
        if posicion_vertice < 0 or posicion_vertice >= self.cantidad_vertices():
            raise ValueError("Error: número de vértice no válido")
    
    # Insertar una arista dirigida (u -> v)
    def insertar_arista(self, pos_vertice_origen, pos_vertice_destino):
        self.validar_vertice(pos_vertice_origen)  # Verificar que el origen sea válido
        self.validar_vertice(pos_vertice_destino)  # Verificar que el destino sea válido
        if self.existe_adyacencia(pos_vertice_origen, pos_vertice_destino):
            raise ValueError("Ya existe adyacencia")
        self.cant_aristas += 1  # Incrementar el contador de aristas
        self.lista_de_adyacencia[pos_vertice_origen].append(pos_vertice_destino)  # Agregar el destino al origen

    # Verificar si existe una conexión (u -> v)
    def existe_adyacencia(self, pos_vertice_origen, pos_vertice_destino):
        self.validar_vertice(pos_vertice_origen)
        self.validar_vertice(pos_vertice_destino)
        adyacencia_del_origen = self.lista_de_adyacencia[pos_vertice_origen]
        return pos_vertice_destino in adyacencia_del_origen

    # Mostrar el grafo dirigido
    def mostrar_grafo_dirigido(self):
        for i in range(len(self.lista_de_adyacencia)):
            vertice = f"[{i}]"  # Representar el vértice actual
            adyacentes = "["  # Representar las conexiones salientes
            for j in self.lista_de_adyacencia[i]:
                adyacentes += f"{j},"  # Agregar los vértices conectados
            if self.lista_de_adyacencia[i]:
                adyacentes = adyacentes[:-1]  # Eliminar la última coma
            adyacentes += "]"
            print(f"{vertice} -> {adyacentes}")

# Ejemplo de uso
if __name__ == "__main__":
    grafo_dirigido = GrafoDirigido()
    
    # Agregar vértices
    grafo_dirigido.insertar_vertice()
    grafo_dirigido.insertar_vertice()
    grafo_dirigido.insertar_vertice()
    grafo_dirigido.insertar_vertice()
    grafo_dirigido.insertar_vertice()
    
    # Agregar aristas dirigidas
    grafo_dirigido.insertar_arista(0, 3)
    grafo_dirigido.insertar_arista(0, 4)
    grafo_dirigido.insertar_arista(1, 2)
    grafo_dirigido.insertar_arista(2, 3)
    grafo_dirigido.insertar_arista(3, 4)
    grafo_dirigido.insertar_arista(4, 1)
    
    # Mostrar el grafo dirigido
    grafo_dirigido.mostrar_grafo_dirigido()
