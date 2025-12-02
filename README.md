# Puesta en Producción Segura
Cristian Fernandez Cornejo | 02/12/2025 TeamVelez

## INSTALACIONES PREVIAS
**Necesitas tener Python 3 instalado en tu sistema**

https://www.python.org/downloads/

**Para instalar las dependencias necesarias:**
```
pip install pytest pytest-cov
```
---

## Ejercicio 2: src/binario.py
Programa que comprueba si algo es binario y lo pasa a decimal.

**Como ejecutarlo:**
```
python src/binario.py
```

Este programa te pedira numeros binarios (101 o 1001), el programa nos los traducira a decimal.

Para salir del programa nos hara falta poner la plabra "exit"

---

## Ejercicio 3: src/lista.py
En este ejercicio tenemos 2 funciones, una para ver si un numero esta en un rango y otra para ver si esta en una lista.

**Como ejecutarlo:**
```
python src/lista.py
```

---

## Ejercicio 4: test/test_unittest.py
Tests usando unittest 

**Como ejecutar los tests:**
```
python -m unittest tests.test_unittest -v
```
El parámetro  -v es para que nos muestre información mas detallada en cada test.

---

## Ejercicio 5: test/test_pytest.py
Tests usando pytest

**Hay que instalar antes pytest con el comando:**
```
pip install pytest
```

**Como ejecutar los tests:**
```
pytest tests/test_pytest.py -v
```
El parámetro  -v es para que nos muestre información mas detallada en cada test.

---

██████╗░██╗░░░██╗████████╗██╗░░██╗░█████╗░███╗░░██╗
██╔══██╗╚██╗░██╔╝╚══██╔══╝██║░░██║██╔══██╗████╗░██║
██████╔╝░╚████╔╝░░░░██║░░░███████║██║░░██║██╔██╗██║
██╔═══╝░░░╚██╔╝░░░░░██║░░░██╔══██║██║░░██║██║╚████║
██║░░░░░░░░██║░░░░░░██║░░░██║░░██║╚█████╔╝██║░╚███║
╚═╝░░░░░░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝