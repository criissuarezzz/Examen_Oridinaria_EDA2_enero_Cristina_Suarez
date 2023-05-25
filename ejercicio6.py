import random

class Pokemon:
    def __init__(self, nombre, tipo, nivel):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel

class Nodo:
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.siguiente = None

class TablaHash:
    def __init__(self):
        self.tabla = [None] * 800

    def _hash(self, clave):
        if isinstance(clave, str):
            return sum(ord(c) for c in clave) % 1000
        else:
            return int(clave) % 1000

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

# Generar los 800 Pokémon
pokemones = []
tipos = ["Agua", "Fuego", "Tierra", "Eléctrico", "Normal", "Fantasma"]

for _ in range(800):
    nombre = "Pokemon" + str(_ + 1)
    tipo = random.choice(tipos)
    nivel = random.randint(1, 100)

    pokemon = Pokemon(nombre, tipo, nivel)
    pokemones.append(pokemon)

print("Se generaron 800 Pokémon.")

# Cargar los Pokémon en las tablas hash
tabla_niveles = TablaHash()
tabla_tipos = TablaHash()

for pokemon in pokemones:
    ultimos_digitos = str(pokemon.nivel)[-3:]
    tabla_niveles.insertar(ultimos_digitos, pokemon)

    iniciales_tipo = pokemon.tipo[:3]
    tabla_tipos.insertar(iniciales_tipo, pokemon)

print("Se cargaron los Pokémon en las tablas hash.")

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


# Obtener los Pokemon de tipo Tierra para que custodien al Profesor Oak en una misión de exploración al Bosque Verdanturf 

# Buscar los Pokémon de tipo Tierra en la tabla hash
pokemones_tierra = []
tipo_tierra = "Tie"

actual = tabla_tipos.tabla[tabla_tipos._hash(tipo_tierra)]

while actual is not None:
    if actual.valor.tipo == tipo_tierra:
        pokemones_tierra.append(actual.valor)
    actual = actual.siguiente

# Mostrar los Pokémon de tipo Tierra encontrados
if len(pokemones_tierra) > 0:
    print("Los Pokémon de tipo Tierra que pueden custodiar al Profesor Oak en el Bosque Verdanturf son:")
    for pokemon in pokemones_tierra:
        print(pokemon.nombre)
else:
    print("No se encontraron Pokémon de tipo Tierra para custodiar al Profesor Oak en el Bosque Verdanturf.")
