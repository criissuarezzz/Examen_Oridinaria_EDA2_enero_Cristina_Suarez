#para ver el problema de las n-pokeballs, primero hay que generar un grafo

class Nodo:
    def __init__(self, fila):
        self.fila = fila
        self.siguiente = None

class Grafo:
    def __init__(self, n):
        self.n = n
        self.nodos = [None] * n
        self.soluciones = []

    def agregar_nodo(self, fila):
        nodo = Nodo(fila)
        if not self.nodos[fila]:
            self.nodos[fila] = nodo
        else:
            actual = self.nodos[fila]
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nodo

    def es_valido(self, fila, columna):
        actual = self.nodos[fila]
        while actual:
            if actual.fila == columna:
                return False
            if abs(actual.fila - columna) == abs(fila - 1):
                return False
            actual = actual.siguiente
        return True

    def backtrack(self, fila):
        if fila == self.n:
            solucion = []
            for i in range(self.n):
                actual = self.nodos[i]
                while actual:
                    solucion.append(actual.fila)
                    actual = actual.siguiente
            self.soluciones.append(solucion)
        else:
            for columna in range(self.n):
                if self.es_valido(fila, columna):
                    self.agregar_nodo(fila)
                    self.backtrack(fila + 1)
                    self.nodos[fila] = self.nodos[fila].siguiente

    def encontrar_soluciones(self):
        self.backtrack(0)

    def imprimir_soluciones(self):
        for solucion in self.soluciones:
            print(solucion)

    def encontrar_solucion(self):
        self.backtrack(0)
        if self.soluciones:
            self.solucion = self.soluciones[0]
            return True
        return False
    

# Imprimir tabla con la posición de una sola bola Pokémon por cada valor de n
print("{:<10s}{:<20s}".format("n", "Posición"))
for n in range(1, 11):
    grafo = Grafo(n)
    if grafo.encontrar_solucion():
        posicion = str(grafo.solucion)
    else:
        posicion = "No hay solución"
    print("{:<10d}{:<20s}".format(n, posicion))

n = 15
grafo = Grafo(n)
if grafo.encontrar_solucion():
    posicion = str(grafo.solucion)
else:
    posicion = "No hay solución"
print("{:<10d}{:<20s}".format(n, posicion))