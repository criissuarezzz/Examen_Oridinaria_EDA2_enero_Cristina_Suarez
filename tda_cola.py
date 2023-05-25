

class Cola():
    """TDA cola """

    def __init__(self):
        self.datos, self.frente, self.final, self.tamanio = [0] * 5, 0, -1, 0


def arribo(cola, dato):
    cola.final += 1 
    cola.datos[cola.final] = dato
    if(cola.final == len(cola.datos)-1):
        cola.final = -1
    cola.tamanio += 1

def atencion(cola):
    aux = cola.datos[cola.frente]
    cola.frente += 1
    if(cola.frente==len(cola.datos)):
        cola.frente = 0
    cola.tamanio -= 1
    return aux

def cola_vacia(cola):
    return cola.tamanio == 0

def cola_llena(cola):
    return cola.tamanio == len(cola.datos)

def tamanio(cola):
    return cola.tamanio

def en_frente(cola):
    return cola.datos[cola.frente]

def mover_final(cola):
    x = atencion(cola)
    arribo(cola, x)
    return x


"""
c = Cola()
caux = Cola()
while not cola_llena(c):
    dato = int(input("ingrese un número"))
    arribo(c, dato)

x = atencion(c)
print("elemento eliminado", x)

if(not cola_llena(c)):
    arribo(c, 100)
while not cola_vacia(c):
    x = atencion(c)
    arribo(caux, x)
    print(x)

while not cola_vacia(caux):
    x = atencion(caux)
    arribo(c, x)

for i in range(0, tamanio(c)):
    print(mover_final(c))

print("fin del barrido")
print(tamanio(c))
"""    