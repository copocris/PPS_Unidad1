"""test_pytest.py tarea 5
Autor: Cristian Fernandez Cornejo
Fecha: 02/12/2025
"""
# importamos las funciones que vamos a probar y pytest
from src.binario import esBinario, binarioADecimal
from src.lista import estaEnRango, estaEnLista
import pytest

# comprobamos que detecta bien binario
def test_binariovalido():
    assert esBinario("1010")
    assert esBinario("1111")
    assert esBinario("0")

# comprobamos que rechaza lo que no sea binario
def test_binarioinvalido():
    assert not esBinario("Hola")
    assert not esBinario("123")
    assert not esBinario("")

# conversion de binario a decimal
def test_conversion():
    assert binarioADecimal("1010") == 10
    assert binarioADecimal("1111") == 15
    assert binarioADecimal("0") == 0

# si pasamos algo que no sea binario nos dara error
def test_conversioninvalida():
    with pytest.raises(ValueError):
        binarioADecimal("Hola")
    with pytest.raises(ValueError):
        binarioADecimal("123")

# miramos si detecta bien los numeros dentro del rango
def test_rangodentro():
    assert estaEnRango(5, 1, 10)
    assert estaEnRango(1, 1, 10)
    assert estaEnRango(10, 1, 10)

# comprobamos que detecte los que estan fuera del rango
def test_rangofuera():
    assert not estaEnRango(15, 1, 10)
    assert not estaEnRango(0, 1, 10)

# verificamos que encuentre elementos que si estan en la lista
def test_listapresente():
    assert estaEnLista(5, [1, 2, 3, 4, 5])
    assert estaEnLista("hola", ["hola", "mundo"])

# probamos que detecte cuando algo no esta en la lista
def test_listaausente():
    assert not estaEnLista(10, [1, 2, 3, 4, 5])
    assert not estaEnLista(5, [])


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
