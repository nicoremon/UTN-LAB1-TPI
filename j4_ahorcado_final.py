# Importamos libreria para elegir la palabra secreta
from random import choice

def ahorcado():

    # Definicion de variables
    palabras = ['juego', 'ahorcado', 'utn', 'programacion', 'villamaria', "cordoba"]
    letras_correctas = []
    letras_incorrectas = []
    intentos = 6
    aciertos = 0
    juego_terminado = False

    # Funcion para elegir la palabra secreta
    def elegir_palabra(lista_palabras):
        palabra_elegida = choice(lista_palabras)
        letras_unicas = len(set(palabra_elegida))

        return palabra_elegida, letras_unicas

    # Funcion para Solicitar letra al usuario y verificar si es valida
    def pedir_letra():
        letra_elegida = ''
        es_valida = False
        abecedario = 'abcdefghijklmnñopqrstuvwxyz'

        while not es_valida:
            letra_elegida = input("Elige una letra: ")
            if letra_elegida in abecedario and len(letra_elegida) == 1:
                es_valida = True
            else:
                print("No has elegido una letra correcta")

        return letra_elegida

    # Funcion para agregar la palabra secreta al array para ser verificado
    def mostrar_nuevo_tablero(palabra_elegida):

        lista_oculta = []

        for l in palabra_elegida:
            if l in letras_correctas:
                lista_oculta.append(l)
            else:
                lista_oculta.append('-')

        print(' '.join(lista_oculta))

    # Funcion para Verificar cada letra ingresada por usuario
    def chequear_letra(letra_elegida, palabra_oculta, vidas, coincidencias):

        fin = False

        if letra_elegida in palabra_oculta and letra_elegida not in letras_correctas:
            letras_correctas.append(letra_elegida)
            coincidencias += 1
        elif letra_elegida in palabra_oculta and letra_elegida in letras_correctas:
            print("Ya ingresaste esa letra, intenta con otra diferente")
        else:
            letras_incorrectas.append(letra_elegida)
            vidas -= 1
            if vidas == 5:
                print('''
                +---+
                |   |
                O   |
                    |
                    |
                    |
                =========
                ''')
            if vidas == 4:
                print('''
                +---+
                |   |
                O   |
                |   |
                    |
                    |
                =========
                ''')
            if vidas == 3:
                print('''
                +---+
                |   |
                O   |
               /|   |
                    |
                    |
                =========
                ''')
            if vidas == 2:
                print('''
                +---+
                |   |
                O   |
               /|\  |
                    |
                    |
                =========
                ''')
            if vidas == 1:
                print('''
                +---+
                |   |
                O   |
               /|\  |
               /    |
                    |
                =========
                ''')
            if vidas == 0:
                print('''
                +---+
                |   |
                O   |
               /|\  |
               / \  |
                    |
                =========
                ''')

        if vidas == 0:
            fin = perder()
        elif coincidencias == letras_unicas:
            fin = ganar(palabra_oculta)

        return vidas, fin, coincidencias

    # funcion para imprimir resultado cuando el jugador pierde
    def perder():
        print("Te has quedado sin vidas")
        print(f"La palabra oculta era {palabra}")

        return True

    # funcion para imprimir resultado cuando el jugador gana
    def ganar(palabra_descubierta):
        mostrar_nuevo_tablero(palabra_descubierta)
        print("Felicitaciones, has encontrado la palabra!!!")

        return True

    palabra, letras_unicas = elegir_palabra(palabras)

    # Juego
    while not juego_terminado:
        if intentos == 6:
            print('\n' + '*' * 20 + '\n')
            print("Bienvenido al Juego del Ahorcado")
            print('\n' + '*' * 20 + '\n')
            print(f'La palabra seleccionada por el sistema cuenta con {len(palabra)} caracteres')
            print('\n')
            mostrar_nuevo_tablero(palabra) # Muestra _ _ _ _ correspondientes a la palabra secreta
            print('\n')
            print('Letras incorrectas: ' + '-'.join(letras_incorrectas))
            print(f'Vidas: {intentos}')
            print('\n' + '*' * 20 + '\n')
            letra = pedir_letra()
        else:
            print('\n' + '*' * 20 + '\n')
            mostrar_nuevo_tablero(palabra) # Muestra _ _ _ _ correspondientes a la palabra secreta
            print('\n')
            print('Letras incorrectas: ' + '-'.join(letras_incorrectas))
            print(f'Vidas: {intentos}')
            print('\n' + '*' * 20 + '\n')
            letra = pedir_letra()

        intentos, terminado, aciertos = chequear_letra(letra,palabra,intentos,aciertos)
        
        juego_terminado = terminado

    print(" ")
    jugar_de_nuevo = input("Quieres volver a Jugar ? (s/n): ")
    if jugar_de_nuevo == 's':
        ahorcado()
    else:
        print(" ")        
        print("\t\tPresiona enter para volver al menu...")
        k=input()    
    



    
