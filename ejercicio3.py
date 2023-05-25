import time
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
        
class Pokeball():
    def __init__(self, peso, nombre, fecha_fabricacion):
        self.peso = peso
        self.nombre = nombre
        self.fecha_fabricacion = fecha_fabricacion
        print("Pokeball creada con exito")

    def __str__(self):
        return "Pokeball: {} de peso {} y fabricada el {}".format(self.nombre, self.peso, self.fecha_fabricacion)


#Crea algunas Pokeballs. Prueba a mostrar los datos de algunas Pokeballs ordenadas por su fecha de fabricación y a modificar algún valor, por ejemplo, prueba a modificar el precio de una de las Pokeballs.
pokeball1 = Pokeball(0.5, "pokeball1", time.strftime("%d/%m/%y"))
pokeball2 = Pokeball(0.6, "pokeball2", time.strftime("%d/%m/%y"))
pokeball3 = Pokeball(0.7, "pokeball3", time.strftime("%d/%m/%y"))
pokeball4 = Pokeball(0.8, "pokeball4", time.strftime("%d/%m/%y"))

#ordenar por fecha de fabricacion
pokeballs = [pokeball1, pokeball2, pokeball3, pokeball4]
pokeballs.sort(key=lambda pokeball: pokeball.fecha_fabricacion)
for pokeball in pokeballs:
    print(pokeball)

import unittest

class TestPokeball(unittest.TestCase):
    def setUp(self):
        self.pokeball1 = Pokeball(0.5, "pokeball1", time.strftime("%d/%m/%y"))
        self.pokeball2 = Pokeball(0.6, "pokeball2", time.strftime("%d/%m/%y"))
        self.pokeball3 = Pokeball(0.7, "pokeball3", time.strftime("%d/%m/%y"))
        self.pokeball4 = Pokeball(0.8, "pokeball4", time.strftime("%d/%m/%y"))

    def test_peso(self):
        self.assertEqual(self.pokeball1.peso, 0.5)
        self.assertEqual(self.pokeball2.peso, 0.6)
        self.assertEqual(self.pokeball3.peso, 0.7)
        self.assertEqual(self.pokeball4.peso, 0.8)

    def test_nombre(self):
        self.assertEqual(self.pokeball1.nombre, "pokeball1")
        self.assertEqual(self.pokeball2.nombre, "pokeball2")
        self.assertEqual(self.pokeball3.nombre, "pokeball3")
        self.assertEqual(self.pokeball4.nombre, "pokeball4")

    def test_fecha_fabricacion(self):
        self.assertEqual(self.pokeball1.fecha_fabricacion, time.strftime("%d/%m/%y"))
        self.assertEqual(self.pokeball2.fecha_fabricacion, time.strftime("%d/%m/%y"))
        self.assertEqual(self.pokeball3.fecha_fabricacion, time.strftime("%d/%m/%y"))
        self.assertEqual(self.pokeball4.fecha_fabricacion, time.strftime("%d/%m/%y"))

    def test_str(self):
        self.assertEqual(str(self.pokeball1), "Pokeball: pokeball1 de peso 0.5 y fabricada el {}".format(time.strftime("%d/%m/%y")))
        self.assertEqual(str(self.pokeball2), "Pokeball: pokeball2 de peso 0.6 y fabricada el {}".format(time.strftime("%d/%m/%y")))
        self.assertEqual(str(self.pokeball3), "Pokeball: pokeball3 de peso 0.7 y fabricada el {}".format(time.strftime("%d/%m/%y")))
        self.assertEqual(str(self.pokeball4), "Pokeball: pokeball4 de peso 0.8 y fabricada el {}".format(time.strftime("%d/%m/%y")))

if __name__ == "__main__":
    unittest.main()