from ejercicio4.tda_cola import Cola, cola_vacia, arribo, atencion
from ejercicio4.tda_heap import Heap, arribo as arribo_h, heap_vacio, atencion as atencion_h
from ejercicio4.tda_heap import cambiar_prioridad, buscar as buscar_h
from ejercicio4.tda_pila_dinamico import Pila, apilar, pila_vacia, desapilar
from math import inf


class nodoArista(object):
    """Clase nodo vértice."""

    def __init__(self, info, destino):
        """Crea un nodo arista con la información cargada."""
        self.info = info
        self.destino = destino
        self.sig = None


class nodoVertice(object):
    """Clase nodo vértice."""

    def __init__(self, info, datos=None):
        """Crea un nodo vértice con la información cargada."""
        self.info = info
        self.datos = datos
        self.sig = None
        self.visitado = False
        self.adyacentes = Arista() # lista de aristas


class Grafo(object):
    """Clase grafo implementación lista de listas de adyacencia."""

    def __init__(self, dirigido=True):
        """Crea un grafo vacio."""
        self.inicio = None
        self.dirigido = dirigido
        self.tamanio = 0


class Arista(object):
    """Clase lista de arsitas implementación sobre lista."""

    def __init__(self):
        """Crea una lista de aristas vacia."""
        self.inicio = None
        self.tamanio = 0


    def insertar_vertice(grafo, dato, datos=None):
        """Inserta un vértice al grafo."""
        nodo = nodoVertice(dato, datos)
        if (grafo.inicio is None or grafo.inicio.info > dato):
            nodo.sig = grafo.inicio
            grafo.inicio = nodo
        else:
            ant = grafo.inicio
            act = grafo.inicio.sig
            while(act is not None and act.info < nodo.info):
                ant = act
                act = act.sig
            nodo.sig = act
            ant.sig = nodo
        grafo.tamanio += 1

    def insertar_arista(grafo, dato, origen, destino):
        """Inserta una arista desde el vértice origen al destino."""
        Arista.agregrar_arista(origen.adyacentes, dato, destino.info)
        if(not grafo.dirigido):
            Arista.agregrar_arista(destino.adyacentes, dato, origen.info)

    def agregrar_arista(origen, dato, destino):
        """Agrega la arista desde el vértice origen al destino."""
        nodo = nodoArista(dato, destino)
        if (origen.inicio is None or origen.inicio.destino > destino):
            nodo.sig = origen.inicio
            origen.inicio = nodo
        else:
            ant = origen.inicio
            act = origen.inicio.sig
            while(act is not None and act.destino < nodo.destino):
                ant = act
                act = act.sig
            nodo.sig = act
            ant.sig = nodo
        origen.tamanio += 1

    def eliminar_vertice(grafo, clave):
        """Elimina un vertice del grafo y lo devuelve si lo encuentra."""
        x = None
        if(grafo.inicio.info == clave):
            x = grafo.inicio.info
            grafo.inicio = grafo.inicio.sig
            grafo.tamanio -= 1
        else:
            ant = grafo.inicio
            act = grafo.inicio.sig
            while(act is not None and act.info != clave):
                ant = act
                act = act.sig
            if (act is not None):
                x = act.info
                ant.sig = act.sig
                grafo.tamanio -= 1
        if(x is not None):
            aux = grafo.inicio
            while(aux is not None):
                if(aux.adyacentes.inicio is not None):
                    Arista.quitar_arista(aux.adyacentes, clave)
                aux = aux.sig
            # aca terminar eliminar aristas adyacenes grafo no dirigido
        return x


    def quitar_arista(vertice, destino):
        x = None
        if(vertice.adyacentes.inicio.destino == destino):
            x = vertice.adyacentes.inicio.info
            vertice.adyacentes.inicio = vertice.adyacentes.inicio.sig
            vertice.adyacentes.tamanio -= 1
        else:
            ant = vertice.adyacentes.inicio
            act = vertice.adyacentes.inicio.sig
            while(act is not None and act.destino != destino):
                ant = act
                act = act.sig
            if (act is not None):
                x = act.info
                ant.sig = act.sig
                vertice.adyacentes.tamanio -= 1
        return x

    def eliminar_arista(grafo, vertice, destino):
        """Elimina una arsita del vertice y lo devuelve si lo encuentra."""
        x = Arista.quitar_arista(vertice, destino)    
        
        if(not grafo.dirigido):
            ori = Arista.buscar_vertice(grafo, destino)
            Arista.quitar_arista(ori, vertice.info)

        return x

    def barrido_vertices(grafo):
        """Realiza un barrido de la grafo mostrando sus valores."""
        aux = grafo.inicio
        while(aux is not None):
            print('vertice:', aux.info)
            print('adyacentes:')
            Arista.adyacentes(aux)
            aux = aux.sig


    def buscar_vertice(grafo, buscado):
        """Devuelve la direccion del elemento buscado."""
        aux = grafo.inicio
        while(aux is not None and aux.info != buscado):
            aux = aux.sig
        return aux

    def buscar_arista(vertice, buscado):
        """Devuelve la direccion del elemento buscado."""
        aux = vertice.adyacentes.inicio
        while(aux is not None and aux.destino != buscado):
            aux = aux.sig
        return aux


    def tamanio(grafo):
        """Devuelve el numero de vertices en el grafo."""
        return grafo.tamanio


    def grafo_vacio(grafo):
        """Devuelve true si el grafo esta vacio."""
        return grafo.inicio is None


    def adyacentes(vertice):
        """Muestra los adyacents del vertice."""
        aux = vertice.adyacentes.inicio
        while(aux is not None):
            print(aux.destino, aux.info)
            aux = aux.sig

    def marcar_no_visitado(grafo):
        """Marca todos losvertices del grafo como no visitados."""
        aux = grafo.inicio
        while(aux is not None):
            aux.visitado = False
            aux = aux.sig

    def barrido_profundidad(grafo, vertice):
        """Barrido en profundidad del grafo."""
        while(vertice is not None):
            if(not vertice.visitado):
                vertice.visitado = True
                print(vertice.info)
                adyacentes = vertice.adyacentes.inicio
                while(adyacentes is not None):
                    adyacente = Arista.buscar_vertice(grafo, adyacentes.destino)
                    if(not adyacente.visitado):
                        Arista.barrido_profundidad(grafo, adyacente)
                    adyacentes = adyacentes.sig
            vertice = vertice.sig

    def barrido_amplitud(grafo, vertice):
        """Barrido en amplitud del grafo."""
        cola = Cola()
        while(vertice is not None):
            if(not vertice.visitado):
                vertice.visitado = True
                arribo(cola, vertice)
                while(not cola_vacia(cola)):
                    nodo = atencion(cola)
                    print(nodo.info)
                    adyacentes = nodo.adyacentes.inicio
                    while(adyacentes is not None):
                        adyacente = Arista.buscar_vertice(grafo, adyacentes.destino)
                        if(not adyacente.visitado):
                            adyacente.visitado = True
                            arribo(cola, adyacente)
                        adyacentes = adyacentes.sig
            vertice = vertice.sig

    def dijkstra(grafo, origen, destino):
        """Algoritmo de Dijkstra para hallar el camino mas corto."""
        no_visitados = Heap(Arista.tamanio(grafo))
        camino = Pila()
        aux = grafo.inicio
        while(aux is not None):
            if(aux.info == origen):
                arribo_h(no_visitados, [aux, None], 0)
            else:
                arribo_h(no_visitados, [aux, None], inf)
            aux = aux.sig

        while(not heap_vacio(no_visitados)):
            dato = atencion_h(no_visitados)
            apilar(camino, dato)
            aux = dato[1][0].adyacentes.inicio
            while(aux is not None):
                pos = buscar_h(no_visitados, aux.destino)
                if(no_visitados.vector[pos][0] > dato[0] + aux.info):
                    no_visitados.vector[pos][1][1] = dato[1][0].info
                    cambiar_prioridad(no_visitados, pos, dato[0] + aux.info)
                aux = aux.sig
        return camino


    def prim(grafo):
        """Algoritmo de Prim para hallar el árbol de expansión mínimo."""
        bosque = []
        aristas = Heap(Arista.tamanio(grafo) ** 2)
        adyac = grafo.inicio.adyacentes.inicio
        while(adyac is not None):
            arribo_h(aristas, [grafo.inicio.info, adyac.destino], adyac.info)
            adyac = adyac.sig
        while(len(bosque) // 2 < Arista.tamanio(grafo) and not heap_vacio(aristas)):
            dato = atencion_h(aristas)
            if(len(bosque) == 0 or ((dato[1][0] not in bosque) ^ (dato[1][1] not in bosque))):
                bosque += dato[1]
                destino = Arista.buscar_vertice(grafo, dato[1][1])
                adyac = destino.adyacentes.inicio
                while(adyac is not None):
                    arribo_h(aristas, [destino.info, adyac.destino], adyac.info)
                    adyac = adyac.sig
        return bosque

    def kruskal(grafo):
        """Algoritmo de Kruskal para hallar el árbol de expansión mínimo."""
        bosque = []
        aristas = Heap(Arista.tamanio(grafo) ** 2)
        aux = grafo.inicio
        while(aux is not None):
            bosque.append([aux.info])
            adyac = aux.adyacentes.inicio
            while(adyac is not None):
                arribo_h(aristas, [aux.info, adyac.destino], adyac.info)
                adyac = adyac.sig
            aux = aux.sig
        while(len(bosque) > 1 and not heap_vacio(aristas)):
            dato = atencion_h(aristas)
            origen = None
            for elemento in bosque:
                if(dato[1][0] in elemento):
                    origen = bosque.pop(bosque.index(elemento))
                    break
            destino = None
            for elemento in bosque:
                if(dato[1][1] in elemento):
                    destino = bosque.pop(bosque.index(elemento))
                    break
            if(origen is not None and destino is not None):
                if(len(origen) > 1 and len(destino) == 1):
                    destino = [dato[1][0], dato[1][1]]
                elif(len(destino) > 1 and len(origen) == 1):
                    origen = [dato[1][0], dato[1][1]]
                elif(len(destino) > 1 and len(origen) > 1):
                    origen += [dato[1][0], dato[1][1]]
                bosque.append(origen + destino)
            else:
                bosque.append(origen)
        return bosque[0]

    def existe_paso(grafo, origen, destino):
        """Barrido en profundidad del grafo."""
        resultado = False
        if(not origen.visitado):
            origen.visitado = True
            vadyacentes = origen.adyacentes.inicio
            while(vadyacentes is not None and not resultado):
                adyacente = Arista.buscar_vertice(grafo, vadyacentes.destino)
                if(adyacente.info == destino.info):
                    return True
                elif(not adyacente.visitado):
                    resultado = Arista.existe_paso(grafo, adyacente, destino)
                vadyacentes = vadyacentes.sig
        return resultado

g = Grafo(False) 

Arista.insertar_vertice(g, 0)
Arista.insertar_vertice(g, 1)
Arista.insertar_vertice(g, 2)
Arista.insertar_vertice(g, 3)
Arista.insertar_vertice(g, 4)
Arista.insertar_vertice(g, 5)
Arista.insertar_vertice(g, 6)
Arista.insertar_vertice(g, 7)
Arista.insertar_vertice(g, 8)
Arista.insertar_vertice(g, 9)

Arista.insertar_arista(g, 1, Arista.buscar_vertice(g, 1), Arista.buscar_vertice(g, 6))  # Teletransporte de Ruta 1 a Ruta 6
Arista.insertar_arista(g, 1, Arista.buscar_vertice(g, 1), Arista.buscar_vertice(g, 8))  # Teletransporte de Ruta 1 a Ruta 8
Arista.insertar_arista(g, 1, Arista.buscar_vertice(g, 2), Arista.buscar_vertice(g, 7))  # Teletransporte de Ruta 2 a Ruta 7
Arista.insertar_arista(g, 1, Arista.buscar_vertice(g, 2), Arista.buscar_vertice(g, 9))  # Teletransporte de Ruta 2 a Ruta 9
Arista.insertar_arista(g, 1, Arista.buscar_vertice(g, 3), Arista.buscar_vertice(g, 4))  # Teletransporte de Ruta 3 a Ruta 4
Arista.insertar_arista(g, 1, Arista.buscar_vertice(g, 3), Arista.buscar_vertice(g, 8))  # Teletransporte de Ruta 3 a Ruta 8
Arista.insertar_arista(g, 1, Arista.buscar_vertice(g, 4), Arista.buscar_vertice(g, 3))  # Teletransporte de Ruta 4 a Ruta 3
Arista.insertar_arista(g, 1, Arista.buscar_vertice(g, 4), Arista.buscar_vertice(g, 9))  # Teletransporte de Ruta 4 a Ruta 9
Arista.insertar_arista(g, 1, Arista.buscar_vertice(g, 4), Arista.buscar_vertice(g, 0))  # Teletransporte de Ruta 4 a Ruta 0
Arista.insertar_arista(g, 1, Arista.buscar_vertice(g, 6), Arista.buscar_vertice(g, 1))  # Teletransporte de Ruta 6 a Ruta 1
Arista.insertar_arista(g, 1, Arista.buscar_vertice(g, 6), Arista.buscar_vertice(g, 7))  # Teletransporte de Ruta 6 a Ruta 7
Arista.insertar_arista(g, 1, Arista.buscar_vertice(g, 6), Arista.buscar_vertice(g, 0))  # Teletransporte de Ruta 6 a Ruta 0
Arista.insertar_arista(g, 1, Arista.buscar_vertice(g, 7), Arista.buscar_vertice(g, 2))  # Teletransporte



def contar_teletransportes_validos(g, ruta_inicial, teletransportes):
    visitados = set()  # Conjunto de rutas visitadas
    contador = 0  # Contador de teletransportes válidos

    # Función auxiliar de búsqueda en profundidad (DFS)
    def dfs(ruta, num_teletransportes):
        nonlocal contador

        visitados.add(ruta)  # Marcar la ruta actual como visitada

        if num_teletransportes == 0:
            contador += 1
        else:
            vecinos = Arista.adyacentes(g, ruta)
            for vecino in vecinos:
                if vecino not in visitados:
                    dfs(vecino, num_teletransportes - 1)

        visitados.remove(ruta)  # Desmarcar la ruta actual como visitada

    dfs(ruta_inicial, teletransportes)
    return contador


# Insertar vértices y aristas según el grafo dado

tabla = []
for ruta_inicial in range(10):
    fila = []
    for teletransportes in range(1, 6):
        contador = contar_teletransportes_validos(g, ruta_inicial, teletransportes)
        fila.append(contador)
    tabla.append(fila)

# Imprimir la tabla
for fila in tabla:
    print(fila)



