"""lista.py Tarea 3
Autor: Cristian Fernandez Cornejo
Fecha: 02/12/2025
"""


def estaEnRango(valor, minimo, maximo):
    # comprueba si un valor esta entre el minimo y el maximo
    return minimo <= valor <= maximo


def estaEnLista(valor, lista):
    # mira si el valor esta dentro de la lista
    return valor in lista


def main():
    # ejemplos de como funciona estaEnRango
    print("Prueba de estaEnRango:")
    print(f"¿5 está en [1, 10]? {estaEnRango(5, 1, 10)}")
    print(f"¿15 está en [1, 10]? {estaEnRango(15, 1, 10)}")
    
    # ejemplos de como funciona estaEnLista
    print("\nPrueba de estaEnLista:")
    numeros = [1, 3, 5, 7, 9]
    print(f"¿5 está en {numeros}? {estaEnLista(5, numeros)}")
    print(f"¿6 está en {numeros}? {estaEnLista(6, numeros)}")


if __name__ == "__main__":
    main()
