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

class Nodo:
    def __init__(self, tarea, duracion):
        self.tarea = tarea
        self.duracion = duracion
        self.tiempo_temprano = 0
        self.tiempo_tardio = 0
        self.sucesores = []

    def agregar_sucesor(self, sucesor):
        self.sucesores.append(sucesor)

def calcular_ruta_critica(inicio):
    # Realizar el Forward Pass
    forward_pass(inicio)

    # Realizar el Backward Pass
    backward_pass(inicio)

    # Identificar la ruta crítica
    ruta_critica = encontrar_ruta_critica(inicio)

    # Calcular la duración mínima del proyecto
    duracion_minima = calcular_duracion_minima(inicio)

    # Obtener la secuencia óptima de tareas
    secuencia_optima = obtener_secuencia_optima(ruta_critica)

    return ruta_critica, duracion_minima, secuencia_optima

def forward_pass(nodo):
    if not nodo.sucesores:
        return nodo.duracion

    max_tiempo_temprano = 0
    for sucesor in nodo.sucesores:
        tiempo_temprano = forward_pass(sucesor)
        max_tiempo_temprano = max(max_tiempo_temprano, tiempo_temprano)

    nodo.tiempo_temprano = max_tiempo_temprano
    return max_tiempo_temprano + nodo.duracion

def backward_pass(nodo):
    if not nodo.sucesores:
        nodo.tiempo_tardio = nodo.tiempo_temprano

    for sucesor in nodo.sucesores:
        sucesor.tiempo_tardio = min(sucesor.tiempo_tardio or nodo.tiempo_tardio - sucesor.duracion, nodo.tiempo_tardio - sucesor.duracion)
        backward_pass(sucesor)

def encontrar_ruta_critica(nodo):
    ruta_critica = []
    if not nodo.sucesores:
        return ruta_critica

    for sucesor in nodo.sucesores:
        if sucesor.tiempo_temprano - sucesor.tiempo_tardio == 0:
            ruta_critica.append((nodo.tarea, sucesor.tarea))
        ruta_critica.extend(encontrar_ruta_critica(sucesor))

    return ruta_critica

def calcular_duracion_minima(nodo):
    if not nodo.sucesores:
        return nodo.duracion

    duracion_minima = 0
    for sucesor in nodo.sucesores:
        duracion_minima = max(duracion_minima, calcular_duracion_minima(sucesor))

    return duracion_minima + nodo.duracion

def obtener_secuencia_optima(ruta_critica):
    secuencia_optima = []
    for tarea in ruta_critica:
        if tarea[0] not in [t[1] for t in secuencia_optima]:
            secuencia_optima.append(tarea)

    return secuencia_optima

# Crear el grafo con los nodos correspondientes a cada tarea y sus duraciones
A = Nodo('A', 20)
B = Nodo('B', 5)
C = Nodo('C', 40)
D = Nodo('D', 10)
E = Nodo('E', 5)
F = Nodo('F', 10)
G = Nodo('G', 20)
H = Nodo('H', 25)
I = Nodo('I', 35)
J = Nodo('J', 25)
K = Nodo('K', 15)
L = Nodo('L', 5)
M = Nodo('M', 25)

# Establecer las dependencias entre tareas
A.agregar_sucesor(B)
A.agregar_sucesor(C)
A.agregar_sucesor(D)
B.agregar_sucesor(E)
B.agregar_sucesor(F)
C.agregar_sucesor(H)
D.agregar_sucesor(M)
E.agregar_sucesor(G)
F.agregar_sucesor(G)
G.agregar_sucesor(I)
G.agregar_sucesor(J)
H.agregar_sucesor(K)
I.agregar_sucesor(K)
J.agregar_sucesor(L)
K.agregar_sucesor(M)

# Calcular la ruta crítica y obtener la secuencia óptima de tareas
ruta_critica, duracion_minima, secuencia_optima = calcular_ruta_critica(A)

# Imprimir resultados
print("Ruta crítica:")
for tarea in ruta_critica:
    print(tarea[0], "->", tarea[1])
print("Duración mínima del proyecto:", duracion_minima)
print("Secuencia óptima de tareas:")
for tarea in secuencia_optima:
    print(tarea[0], "->", tarea[1])
