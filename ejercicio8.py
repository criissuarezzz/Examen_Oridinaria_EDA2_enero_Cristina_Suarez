class Nodo:
    def __init__(self, tarea, duracion):
        self.tarea = tarea
        self.duracion = duracion
        self.tiempo_temprano = None
        self.tiempo_tardio = None
        self.sucesores = []

    def agregar_sucesor(self, sucesor):
        self.sucesores.append(sucesor)

class Grafo:
    def __init__(self):
        self.nodos = {}

    def agregar_nodo(self, tarea, duracion):
        nodo = Nodo(tarea, duracion)
        self.nodos[tarea] = nodo

    def agregar_dependencia(self, tarea_origen, tarea_destino):
        origen = self.nodos[tarea_origen]
        destino = self.nodos[tarea_destino]
        origen.agregar_sucesor(destino)

    def calcular_ruta_critica(self, inicio):
        # Realizar el Forward Pass
        self.forward_pass(inicio)

        # Realizar el Backward Pass
        self.backward_pass(inicio)

        # Identificar la ruta crítica
        ruta_critica = self.encontrar_ruta_critica(inicio)

        # Calcular la duración mínima del proyecto
        duracion_minima = self.calcular_duracion_minima(inicio)

        # Obtener la secuencia óptima de tareas
        secuencia_optima = self.obtener_secuencia_optima(ruta_critica)

        return ruta_critica, duracion_minima, secuencia_optima

    def forward_pass(self, nodo):
        if nodo.tiempo_temprano is not None:
            return nodo.tiempo_temprano

        max_tiempo_temprano = 0
        for sucesor in nodo.sucesores:
            tiempo_temprano = self.forward_pass(sucesor)
            max_tiempo_temprano = max(max_tiempo_temprano, tiempo_temprano)

        nodo.tiempo_temprano = max_tiempo_temprano + nodo.duracion
        return nodo.tiempo_temprano

    def backward_pass(self, nodo, tiempo_tardio_padre):
        if nodo.tiempo_tardio is not None:
            return nodo.tiempo_tardio

        nodo.tiempo_tardio = tiempo_tardio_padre - nodo.duracion if tiempo_tardio_padre is not None else nodo.tiempo_temprano

        for sucesor in nodo.sucesores:
            self.backward_pass(sucesor, nodo.tiempo_tardio)

    def encontrar_ruta_critica(self, nodo):
        ruta_critica = []
        if not nodo.sucesores:
            return ruta_critica

        for sucesor in nodo.sucesores:
            if sucesor.tiempo_temprano - sucesor.tiempo_tardio == 0:
                ruta_critica.append((nodo.tarea, sucesor.tarea))
            ruta_critica.extend(self.encontrar_ruta_critica(sucesor))

        return ruta_critica

    def calcular_duracion_minima(self, nodo):
        if not nodo.sucesores:
            return nodo.duracion

        duracion_minima = 0
        for sucesor in nodo.sucesores:
            duracion_minima = max(duracion_minima, self.calcular_duracion_minima(sucesor))

        return duracion_minima + nodo.duracion

    def obtener_secuencia_optima(self, ruta_critica):
        secuencia_optima = []
        for tarea in ruta_critica:
            if tarea[0] not in [t[1] for t in secuencia_optima]:
                secuencia_optima.append(tarea)

        return secuencia_optima


# Crear el grafo
grafo = Grafo()

# Agregar los nodos correspondientes a cada tarea y sus duraciones
grafo.agregar_nodo('A', 20)
grafo.agregar_nodo('B', 5)
grafo.agregar_nodo('C', 40)
grafo.agregar_nodo('D', 10)
grafo.agregar_nodo('E', 5)
grafo.agregar_nodo('F', 10)
grafo.agregar_nodo('G', 20)
grafo.agregar_nodo('H', 25)
grafo.agregar_nodo('I', 35)
grafo.agregar_nodo('J', 25)
grafo.agregar_nodo('K', 15)
grafo.agregar_nodo('L', 5)
grafo.agregar_nodo('M', 25)

# Establecer las dependencias entre tareas
grafo.agregar_dependencia('A', 'B')
grafo.agregar_dependencia('A', 'C')
grafo.agregar_dependencia('A', 'D')
grafo.agregar_dependencia('B', 'E')
grafo.agregar_dependencia('B', 'F')
grafo.agregar_dependencia('C', 'G')
grafo.agregar_dependencia('D', 'G')
grafo.agregar_dependencia('E', 'H')
grafo.agregar_dependencia('F', 'H')
grafo.agregar_dependencia('G', 'I')
grafo.agregar_dependencia('H', 'J')
grafo.agregar_dependencia('I', 'K')
grafo.agregar_dependencia('J', 'K')
grafo.agregar_dependencia('K', 'L')
grafo.agregar_dependencia('L', 'M')

# Calcular la ruta crítica y la duración mínima
ruta_critica, duracion_minima, secuencia_optima = grafo.calcular_ruta_critica(grafo.nodos['A'])

# Imprimir los resultados
print("Ruta Crítica:")
for tarea in ruta_critica:
    print(tarea[0], "->", tarea[1])

print("Duración mínima del proyecto:", duracion_minima)

print("Secuencia óptima de tareas:")
for tarea in secuencia_optima:
    print(tarea[0], "->", tarea[1])
