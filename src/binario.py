"""binario.py Tarea 2
Autor: Cristian Fernandez Cornejo
Fecha: 02/12/2025
"""
# importamos os para obtener el nombre del usuario en el sistema (para que quede mas bonito el código, realmente esto es solo estetico)
import os


def esBinario(strbinario):
    # si esta vacio o no es texto, entonces no es binario
    if not strbinario or not isinstance(strbinario, str):
        return False
    
    # miramos cada letra que tenga la cadena
    for caracter in strbinario:
        # si hay algo que no sea 0 o 1 entonces no es binario
        if caracter not in ('0', '1'):
            return False
    
    return True


def binarioADecimal(strbinario):
    # antes de convertir revisamos que sea binario de verdad
    if not esBinario(strbinario):
        raise ValueError(f"'{strbinario}' no es un número binario, revisalo por favor.")
    
    # convertimos usando int() con base 2 para interpretar el numero como binario
    return int(strbinario, 2)


def main():
    # Se repite el bucle while hasta que el usuario decida salir
    while True:
        print("porfa pon un número binario o sino introduce la palabra 'exit' para salir:")
        numero = input().strip()
        
        # si escribes exit salimos del bucle, antes importamos os para obtener el nombre del usuario en el sistema.
        if numero == "exit":
            usuario = os.getenv("USERNAME") or os.getenv("USER") or "usuario"
            print(f"saliendo de este programa tan bueno :(.... te echaremos de menos :( {usuario}")
            break
        
        # limpiamos el terminal despues de introducir el numero (para que nos quede mas estetico, tambien es opcional)
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # comprobamos si el numero es binario
        if esBinario(numero):
            decimal = binarioADecimal(numero)
            print(f"Tu numero binario: {numero} en decimas es: {decimal}")
        else:
            # si resulta que no es binario enseñamos un ejemplo al usuario
            print(f"'{numero}' no es un número binario (101) y (1100) son ejemplos de números binarios válidos.")


if __name__ == "__main__":
    main()
