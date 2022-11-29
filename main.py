# Importar Juegos y la funcion del juego
from j1_adivinaNum_final import adivinaNumero
from j2_ppt_final import ppt
from j3_21_final import blackjack
from j4_ahorcado_final import ahorcado

# Presentacion TPI
print(' ')
print("**************************************************")
print("********** Trabajo Practico Integrador  **********")
print("***** Alumnos: Trucco - Torres - Tossolini - Remon")
print("**************************************************")
print(' ')

# Funcion para comprobar que se ingresen solo datos correctos (Numeros del 1 al 5)
def opcion_menu():
    while True:
        opcion = 0
        opciones = [1,2,3,4,5]
        try:
            opcion = int(input("Ingresa la opcion: "))
        except ValueError:
            print("Debes escribir un número entre 1 y 5.")
            continue

        if opcion not in opciones:
            print("Debes escribir un número entre 1 y 5.")
            continue
        else:
            break

    return opcion

# Funcion Menu
def menu():
    eleccion = 0
    print(' ')
    print('¿Que juego quieres jugar?')
    print(' ')
    print('1 > Adivina un numero')
    print('2 > Piedra Papel Tijera')
    print('3 > 21 BlackJack')
    print('4 > Ahorcado')
    print('5 > Salir')
    print(' ')
    
    if eleccion == 0:
        eleccion = opcion_menu()
    if int(eleccion) == 1:
        adivinaNumero()
        menu()
    elif int(eleccion) == 2:
        ppt()
        menu()
    elif int(eleccion) == 3:
        blackjack()
        menu()
    elif int(eleccion) == 4:
        ahorcado()
        menu()
    elif int(eleccion) == 5:
        print('Gracias por Jugar!')

# Ejecuto funcion        
menu()