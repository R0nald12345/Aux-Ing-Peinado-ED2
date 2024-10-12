# from ClaseNodoMvias import NodoMVias
from ClaseArbolMVias import ArbolMViasBusqueda

def main():
    # Crear un árbol M-Vías con un orden de 3
    arbol = ArbolMViasBusqueda(orden=3)

    # Insertar algunos números en el árbol
    numeros_a_insertar = [10, 20, 30, 5, 15, 25, 35]
    
    print("Insertando números:")
    for numero in numeros_a_insertar:
        arbol.insertar(numero)  # Inserta solo el número
        print(f"Número {numero} insertado.")

    # Mostrar el recorrido en in-orden
    print("Recorrido en in-orden:")
    recorrido = arbol.recorrido_en_in_orden()
    print(recorrido)  # Imprimir el recorrido en in-orden

    # Mostrar la altura del árbol
    altura = arbol.altura()
    print(f"Altura del árbol: {altura}")

if __name__ == "__main__":
    main()
