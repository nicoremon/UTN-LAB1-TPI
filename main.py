# Importar Juegos y la funcion del juego
from j1_adivinaNum_final import adivinaNumero
from j2_ppt_final import ppt
from j3_21_final import blackjack
from j4_ahorcado_final import ahorcado


print(' ')
print("**************************************************")
print("********** Trabajo Practico Integrador  **********")
print("***** Alumnos: Trucco - Torres - Tossolini - Remon")
print("**************************************************")
print(' ')

def opcion_menu():
    es_valido = False
    opciones = [1,2,3,4,5]
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'
    while not es_valido:
        opcion = input("Ingresa la opcion: ")
        if opcion not in abecedario and len(opcion) == 1:
            if int(opcion) in opciones:
                es_valido = True
            else:
                print("No has elegido una opcion correcta, vuelve a intentar")

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