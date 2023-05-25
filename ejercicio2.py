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
        
    def __str__(self):
        return "Pokemon: {} de tipo {}".format(self.nombre, self.tipo)
        

#experimentacion con unittest
import unittest

class TestPokemon(unittest.TestCase):
    def setUp(self):
        self.pokemon1 = Pokemon("Pikachu", "PS")
        self.pokemon2 = Pokemon("Charmander", "Ataque")
        self.pokemon3 = Pokemon("Squirtle", "Defensa")
        self.pokemon4 = Pokemon("Bulbasaur", "Ataque Especial")

    def test_clasificacion(self):
        self.assertEqual(self.pokemon1.clasificacion(), "Pokemon de tipo PS")
        self.assertEqual(self.pokemon2.clasificacion(), "Pokemon de tipo Ataque")
        self.assertEqual(self.pokemon3.clasificacion(), "Pokemon de tipo Defensa")
        self.assertEqual(self.pokemon4.clasificacion(), "Pokemon de tipo Ataque Especial")

    def test_nombre(self):
        self.assertEqual(self.pokemon1.nombre, "Pikachu")
        self.assertEqual(self.pokemon2.nombre, "Charmander")
        self.assertEqual(self.pokemon3.nombre, "Squirtle")
        self.assertEqual(self.pokemon4.nombre, "Bulbasaur")

    def test_tipo(self):
        self.assertEqual(self.pokemon1.tipo, "PS")
        self.assertEqual(self.pokemon2.tipo, "Ataque")
        self.assertEqual(self.pokemon3.tipo, "Defensa")
        self.assertEqual(self.pokemon4.tipo, "Ataque Especial")

    def test_str(self):
        self.assertEqual(str(self.pokemon1), "Pokemon: Pikachu de tipo PS")
        self.assertEqual(str(self.pokemon2), "Pokemon: Charmander de tipo Ataque")
        self.assertEqual(str(self.pokemon3), "Pokemon: Squirtle de tipo Defensa")
        self.assertEqual(str(self.pokemon4), "Pokemon: Bulbasaur de tipo Ataque Especial")

    def tearDown(self):
        del(self.pokemon1)
        del(self.pokemon2)
        del(self.pokemon3)
        del(self.pokemon4)

    

if __name__ == "__main__":
    unittest.main()