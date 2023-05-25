class Grafo:
    def __init__(self, n):
        self.n = n
        self.posiciones = [None] * n

    def es_valido(self, fila, columna):
        for i in range(self.n):
            if self.posiciones[i] is not None:
                if self.posiciones[i][1] == columna:  # Verificar misma columna
                    return False
                if abs(self.posiciones[i][0] - fila) == abs(self.posiciones[i][1] - columna):  # Verificar diagonales
                    return False
        return True

    def backtrack(self, fila):
        if fila == self.n:
            return True
        for columna in range(self.n):
            if self.es_valido(fila, columna):
                self.posiciones[fila] = (fila, columna)
                if self.backtrack(fila + 1):
                    return True
                self.posiciones[fila] = None
        return False

    def encontrar_solucion(self):
        if self.backtrack(0):
            return self.posiciones
        return None


def imprimir_tabla():
    print("{:<10s}{:<20s}".format("n", "Posición"))
    for n in range(1, 11):
        grafo = Grafo(n)
        solucion = grafo.encontrar_solucion()
        if solucion:
            posicion = str(solucion)
        else:
            posicion = "No hay solución"
        print("{:<10d}{:<20s}".format(n, posicion))

imprimir_tabla()

#para n=15

grafo=Grafo(15)
solucion=grafo.encontrar_solucion()
print(solucion)