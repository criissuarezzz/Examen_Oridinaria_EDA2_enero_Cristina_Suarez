import csv

class Pokemon():
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        print("Pokemon creado con exito")

    def clasificacion(self):
        if self.tipo == "PS":
            return "Pokemon de tipo PS"
        elif self.tipo == "Ataque" or self.tipo == "ataque":
            return "Pokemon de tipo Ataque"
        elif self.tipo == "Defensa" or self.tipo == "defensa":
            return "Pokemon de tipo Defensa"
        elif self.tipo == "Ataque Especial" or self.tipo == "ataque especial":
            return "Pokemon de tipo Ataque Especial"
        elif self.tipo == "Defensa Especial" or self.tipo == "defensa especial":
            return "Pokemon de tipo Defensa Especial"
        elif self.tipo == "Velocidad" or self.tipo == "velocidad":
            return "Pokemon de tipo Velocidad"
        
def anadir_pokemon(nombre, tipo):
    with open("pokemon.csv", "a") as archivo:
        archivo.write("{},{}\n".format(nombre, tipo))
    print("Pokemon añadido con exito")

def leer_pokemon():
    with open("pokemon.csv", "r") as archivo:
        lector = csv.reader(archivo)
        for linea in lector:
            print(linea)

pokemon1 = Pokemon("Pikachu", "PS")
anadir_pokemon(pokemon1.nombre, pokemon1.tipo)

pokemon2 = Pokemon("Charmander", "Ataque")
anadir_pokemon(pokemon2.nombre, pokemon2.tipo)

pokemon3 = Pokemon("Squirtle", "Defensa")
anadir_pokemon(pokemon3.nombre, pokemon3.tipo)

pokemon4 = Pokemon("Bulbasaur", "Ataque Especial")
anadir_pokemon(pokemon4.nombre, pokemon4.tipo)

#experimentacion con unittest
import unittest

class TestPokemon(unittest.TestCase):
    def setUp(self):
        self.pokemon = Pokemon("Pikachu", "PS")

    def test_clasificacion(self):
        self.assertEqual(self.pokemon.clasificacion(), "Pokemon de tipo PS")

    def test_nombre(self):
        self.assertEqual(self.pokemon.nombre, "Pikachu")

    def test_tipo(self):
        self.assertEqual(self.pokemon.tipo, "PS")

    def tearDown(self):
        del(self.pokemon)

if __name__ == "__main__":
    unittest.main()