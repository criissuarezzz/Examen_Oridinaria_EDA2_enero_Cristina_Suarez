import random

class Pokemon:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        print("Pokemon creado con exito")


class Nodo:
    def __init__(self, clave, valor):
        self. clave = clave
        self.valor = valor
        self.siguiente = None

class TablaHash:
    def __init__(self):
        self.tabla=[None]*1000

    def hash(self, clave):
        return int(clave)%1000
    
    def insertar(self, clave, valor):
        indice = self._hash(clave)
        nodo = Nodo(clave, valor)

        if self.tabla[indice] is None:
            self.tabla[indice] = nodo
        else:
            actual = self.tabla[indice]
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nodo

    def buscar(self, clave):
        indice = self._hash(clave)
        actual = self.tabla[indice]

        while actual is not None:
            if actual.clave == clave:
                return actual.valor
            actual = actual.siguiente

        return None

    def eliminar(self, clave):
        indice = self._hash(clave)
        actual = self.tabla[indice]
        previo = None

        while actual is not None:
            if actual.clave == clave:
                if previo is None:
                    self.tabla[indice] = actual.siguiente
                else:
                    previo.siguiente = actual.siguiente
                return True
            previo = actual
            actual = actual.siguiente

        return False
    

pokemon=[]
tipos= ["Agua", "Fuego", "Tierra", "Electrico", "Normal", "Fantasma"]
for i in range(800):
    nombre = "Pokemon" + str(i + 1)
    tipo = random.choice(tipos)
    nivel = random.randint(1, 100)

    pokemon = Pokemon(nombre, tipo, nivel)
    pokemon.append(pokemon)

print("Se han creado 800 pokemones con exito")




tabla_niveles = TablaHash()
tabla_tipos = TablaHash()

for pokemon in pokemon:
    ultimos_digitos = str(pokemon.nivel)[-3:]
    tabla_niveles.insertar(ultimos_digitos, pokemon)

    iniciales_tipo = pokemon.tipo[:3]
    tabla_tipos.insertar(iniciales_tipo, pokemon)

print("Se han añadido los pokemones a las tablas hash con exito")


# Determinar si el Pokémon Fantasma de nivel 187 está cargado y eliminarlo
pokemon_desertor = tabla_tipos.buscar("Fan")
if pokemon_desertor is not None and pokemon_desertor.nivel == 187:
    tabla_niveles.eliminar(str(pokemon_desertor.nivel)[-3:])
    tabla_tipos.eliminar("Fan")
    print("El Pokémon Fantasma de nivel 187 fue encontrado y eliminado.")
else:
    print("El Pokémon Fantasma de nivel 187 no se encontró.")

# Obtener los Pokémon terminados en 78 para asignarlos a una misión de asalto
pokemones_asalto = []

for clave in tabla_niveles.tabla:
    actual = clave
    while actual is not None:
        if actual.clave[-2:] == "78":
            pokemones_asalto.append(actual.valor)
        actual = actual.siguiente

if pokemones_asalto:
    print("Pokémon terminados en 78 asignados a la misión de asalto:")
    for pokemon in pokemones_asalto:
        print(f"Nombre: {pokemon.nombre}, Tipo: {pokemon.tipo}, Nivel: {pokemon.nivel}")
else:
    print("No se encontraron Pokémon terminados en 78.")

# Obtener los Pokémon terminados en 37 para una misión de exploración
pokemones_exploracion = []

for clave in tabla_niveles.tabla:
    actual = clave
    while actual is not None:
        if actual.clave[-2:] == "37":
            pokemones_exploracion.append(actual.valor)
        actual = actual.siguiente

if pokemones_exploracion:
    print("Pokémon terminados en 37 asignados a la misión de exploración:")
    for pokemon in pokemones_exploracion:
        print(f"Nombre: {pokemon.nombre}, Tipo: {pokemon.tipo}, Nivel: {pokemon.nivel}")
else:
    print("No se encontraron Pokémon terminados en 37.")