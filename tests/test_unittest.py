"""test_unittest.py tarea 4
Autor: Cristian Fernandez Cornejo
Fecha: 02/12/2025
"""
# importamos las funciones que vamos a probar y unittest
from src.binario import esBinario, binarioADecimal
from src.lista import estaEnRango, estaEnLista
import unittest


class TestEsBinario(unittest.TestCase):
    
    # probamos con binarios que si son validos
    def test_binariosvalidos(self):
        self.assertTrue(esBinario("1100"))
        self.assertTrue(esBinario("1"))
        self.assertTrue(esBinario("10101"))
    
    # probamos con cosas que no son binarias
    def test_cadenasinvalidas(self):
        self.assertFalse(esBinario("Python"))
        self.assertFalse(esBinario("789"))
        self.assertFalse(esBinario(""))
        self.assertFalse(esBinario("11x0"))


class TestBinarioADecimal(unittest.TestCase):
    
    # miramos si convierte bien los binarios
    def test_conversioncorrecta(self):
        self.assertEqual(binarioADecimal("1100"), 12)
        self.assertEqual(binarioADecimal("10101"), 21)
        self.assertEqual(binarioADecimal("1"), 1)
    
    # si le pasamos basura debe lanzar error
    def test_binarioinvalido(self):
        with self.assertRaises(ValueError):
            binarioADecimal("Test")
        with self.assertRaises(ValueError):
            binarioADecimal("456")


class TestEstaEnRango(unittest.TestCase):
    
    # comprobamos valores que si estan dentro
    def test_valoresenrango(self):
        self.assertTrue(estaEnRango(7, 2, 15))
        self.assertTrue(estaEnRango(2, 2, 15))
        self.assertTrue(estaEnRango(15, 2, 15))
    
    # comprobamos valores que estan fuera
    def test_valoresfuerarango(self):
        self.assertFalse(estaEnRango(20, 2, 15))
        self.assertFalse(estaEnRango(1, 2, 15))


class TestEstaEnLista(unittest.TestCase):
    
    # buscamos cosas que si estan en la lista
    def test_elementopresente(self):
        self.assertTrue(estaEnLista(8, [2, 4, 6, 8, 10]))
        self.assertTrue(estaEnLista("kamehameha", ["rasengan", "kamehameha", "bankai"]))
    
    # buscamos cosas que no estan en la lista
    def test_elementoausente(self):
        self.assertFalse(estaEnLista(7, [2, 4, 6, 8, 10]))
        self.assertFalse(estaEnLista("chidori", ["rasengan", "kamehameha", "bankai"]))
        self.assertFalse(estaEnLista(3, []))


if __name__ == "__main__":
    unittest.main()
