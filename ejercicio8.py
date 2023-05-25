"""
Eres uno de los líderes de gimnasio (Gym Leader) de una importante organización Pokémon internacional. Uno de los altos miembros del Alto Mando te informa que el Campeón de la Liga Pokémon ha viajado desde EEUU a Barcelona y ha convocado un torneo de alto nivel para esta tarde a las 19:30 en Barcelona. Han consultado la lista de vuelos desde Madrid (donde estás tú) y han llegado a la conclusión de que tienes que tomar un vuelo que parte de Madrid dentro de 2 horas y cierra su facturación 20 minutos antes.

¿Qué duración mínima tiene la misión? ¿Llega el líder a facturar a tiempo dentro de los 100 minutos disponibles? Si no es así, revisa las dependencias, seguro que estás indicando relaciones basadas en las restricciones de los recursos.

Coloca primero la ruta crítica y sus recursos necesarios. A continuación, coloca y reajusta el resto de las actividades dentro de su holgura y define quién hará qué actividad.


Aquí tienes la tabla generada a partir de los datos proporcionados:

TAREA

DESCRIPCIÓN

DURACIÓN

A

Llamar a la agencia de viajes, reservar una plaza y recibir la conformidad.

20'

B

Llamar a casa para que preparen a los Pokémon.

5'

C

Preparar a los Pokémon.

40'

D

La agencia de viajes prepara el billete.

10'

E

Ir desde el gimnasio a la agencia de viajes a recoger los billetes.

5'

F

Recoger los billetes de la agencia y llevarlos al gimnasio.

10'

G

Ir desde el gimnasio a casa a recoger a los Pokémon.

20'

H

Recoger a los Pokémon y llevarlos al gimnasio.

25'

I

Conversar con los colaboradores para obtener información sobre qué Pokémon llevar en este viaje.

35'

J

Seleccionar los Pokémon más fuertes y dejar instrucciones para el tiempo de la ausencia.

25'

K

Reunir los objetos más importantes para llevar en este viaje.

15'

L

Organizar los objetos.

5'

M

Viajar al aeropuerto y facturar.

25'

 

Ahora que tienes una lista de tareas y sus respectivas duraciones, necesitas decidir el camino más corto para completarlas todas. Considera cada tarea como un nodo y la duración como el peso de la arista que conecta las tareas. Algunas tareas deben completarse antes que otras, lo que implica que los nodos no están todos conectados entre sí.

Determinar la secuencia óptima de tareas. Recuerda que estos algoritmos son útiles para encontrar el árbol de expansión mínima en un grafo, lo que en este caso representaría la secuencia de tareas con el tiempo total mínimo.

¿Cuál algoritmo elegirías en este caso y por qué? Desarrolla y describe el proceso que utilizarías para aplicar este algoritmo al conjunto de tareas.
"""

class Tarea:
    def __init__(self, nombre, duracion):
        self.nombre = nombre
        self.duracion = duracion

    def __repr__(self):
        return self.nombre
    
tareas = [
    Tarea("A", 20),
    Tarea("B", 5),
    Tarea("C", 40),
    Tarea("D", 10),
    Tarea("E", 5),
    Tarea("F", 10),
    Tarea("G", 20),
    Tarea("H", 25),
    Tarea("I", 35),
    Tarea("J", 25),
    Tarea("K", 15),
    Tarea("L", 5),
    Tarea("M", 25),
]

dependencias = [
    ('A', 'D'),
    ('A', 'E'),
    ('D', 'F'),
    ('E', 'F'),
    ('B', 'G'),
    ('G', 'H'),
    ('C', 'H'),
    ('H', 'J'),
    ('F', 'J'),
    ('I', 'J'),
    ('K', 'L'),
    ('J', 'M')
]

class Arista:
    def __init__(self, origen, destino, peso):
        self.origen = origen
        self.destino = destino
        self.peso = peso

class GrafoDirigidoPonderado:
    def __init__(self):
        self.nodos={}
        self.aristas=[]

    def agregar_nodo(self, nombre, duracion):
        tarea = Tarea(nombre, duracion)
        self.nodos[nombre] = tarea

    def agregar_arista(self, origen, destino, peso):
        arista = Arista(origen, destino, peso)
        self.aristas.append(arista)

    def obtener_tarea(self, nombre):
        return self.nodos[nombre]

    def obtener_duraciones(self):
        duraciones = {}
        for tarea in self.nodos.values():
            duraciones[tarea] = tarea.duracion
        return duraciones
    
# Creamos el grafo
grafo = GrafoDirigidoPonderado()

# Agregamos los nodos
for tarea in tareas:
    grafo.agregar_nodo(tarea.nombre, tarea.duracion)

# Agregamos las aristas
for dependencia in dependencias:
    origen = dependencia[0]
    destino = dependencia[1]
    peso = grafo.obtener_tarea(destino).duracion
    grafo.agregar_arista(origen, destino, peso)


def forward_pass(grafo):
    duraciones = grafo.obtener_duraciones()

    # Inicializar los tiempos tempranos de todas las tareas en 0
    tiempos_tempranos = {tarea: 0 for tarea in duraciones}

    # Recorrer el grafo en orden topológico calculando los tiempos tempranos
    for tarea in grafo.nodos.values():
        for arista in grafo.aristas:
            if arista.destino == tarea.nombre:
                tiempo_temprano = tiempos_tempranos[arista.origen] + duraciones[arista.origen]
                if tiempo_temprano > tiempos_tempranos[tarea]:
                    tiempos_tempranos[tarea] = tiempo_temprano

    return tiempos_tempranos


def backward_pass(grafo, tiempos_tempranos):
    duraciones = grafo.obtener_duraciones()

    # Inicializar los tiempos tardíos de todas las tareas en el tiempo temprano de la última tarea
    tiempos_tardios = {tarea: tiempos_tempranos[list(grafo.nodos.values())[-1]] for tarea in duraciones}

    # Recorrer el grafo en orden topológico inverso calculando los tiempos tardíos
    for tarea in reversed(list(grafo.nodos.values())):
        for arista in grafo.aristas:
            if arista.origen == tarea.nombre:
                tiempo_tardio = tiempos_tardios[arista.destino] - duraciones[tarea]
                if tiempo_tardio < tiempos_tardios[tarea]:
                    tiempos_tardios[tarea] = tiempo_tardio

    return tiempos_tardios


def encontrar_ruta_critica(grafo,tiempos_tempranos, tiempos_tardios):
    ruta_critica = []

    for tarea in grafo.nodos.values():
        tiempo_temprano = tiempos_tempranos[tarea]
        tiempo_tardio = tiempos_tardios[tarea]

        if tiempo_temprano == tiempo_tardio:
            ruta_critica.append(tarea)

    return ruta_critica

# Calcular la duración mínima del proyecto sumando las duraciones de las tareas en la ruta crítica
def calcular_duracion_minima(ruta_critica):
    duracion_minima = 0
    for tarea in ruta_critica:
        duracion_minima += tarea.duracion

    return duracion_minima

# Obtener la secuencia óptima de tareas siguiendo el camino de la ruta crítica
def obtener_secuencia_optima(ruta_critica):
    secuencia_optima = []

    for tarea in ruta_critica:
        secuencia_optima.append(tarea)

    return secuencia_optima


# Realizar el Forward Pass y el Backward Pass
tiempos_tempranos = forward_pass(grafo)
tiempos_tardios = backward_pass(grafo, tiempos_tempranos)

# Identificar la ruta crítica
ruta_critica = encontrar_ruta_critica(grafo, tiempos_tempranos, tiempos_tardios)

# Calcular la duración mínima del proyecto
duracion_minima = calcular_duracion_minima(ruta_critica)

# Obtener la secuencia óptima de tareas
secuencia_optima = obtener_secuencia_optima(ruta_critica)

# Imprimir los resultados
print("Tiempos Tempranos:")
for tarea, tiempo in tiempos_tempranos.items():
    print(f"{tarea}: {tiempo}")

print("\nTiempos Tardíos:")
for tarea, tiempo in tiempos_tardios.items():
    print(f"{tarea}: {tiempo}")

print("\nRuta Crítica:")
for tarea in ruta_critica:
    print(tarea)

print("\nDuración Mínima del Proyecto:", duracion_minima)

print("\nSecuencia Óptima de Tareas:")
for tarea in secuencia_optima:
    print(tarea)