import random

def ppt():

    #Para que el juego quede mas personalizado le pedimos al jugador su nombre
    print(' ')
    nombre = input("Hola vamos a Jugar a Piedra Papel Tijeras, mi nombre es Pc. ¿Y tú, cómo te  llamas ? ")
    print(' ')
    print(f"Encantado de conocerte {nombre}")
    print(' ')
    print("Empezamos...")
    print(' ')

    # Definicion de Variables del juego
    victorias_jugador = 0
    victorias_pc = 0

    ganando = 0
    perdiendo = 0

    Maxju = 0

    jugando = True

    # Funcion para validar que el numero ingresado este entre 1 y 3 y no sea una letra
    def opcion():
        es_valido = False
        numeros = [1,2,3]
        abecedario = 'abcdefghijklmnñopqrstuvwxyz'
        while not es_valido:
            opcion = input("Elige tu opcion: 1 (Piedra) - 2 (Papel) - 3 (Tijeras) ")
            if opcion not in abecedario and len(opcion) == 1:
                if int(opcion) in numeros:
                    es_valido = True
            else:
                print("No has elegido una opcion correcta, vuelve a intentar")

        return opcion

    #elegir eleatorio -random- elegir jugador.
    # Tambien se puede usar random.randrange (1, 4) el 4 no es considerado.
    while jugando:
        # En cada ciclo se genera una opcion aleatoria para la PC
        aleatorio = random.randint(1, 3)
        Pc = ""
        Usuario = ""

        # Se llama a la funcion que brinda las opciones al usuario
        eleccion = opcion()

        #aqui comienza el recorrido de la eleccion del usuario
        if int(eleccion) == 1:
            Usuario = "Piedra"
        elif int(eleccion) == 2:
            Usuario = "Papel"
        elif int(eleccion) == 3:
            Usuario = "Tijeras"
        print("Elejiste: ", Usuario)

        # Opciones PC
        if aleatorio == 1:
            Pc = "Piedra"
        elif aleatorio == 2:
            Pc = "Papel"
        elif aleatorio == 3:
            Pc = "Tijeras"
        print("Yo elegi: ", Pc)

    
    # Compara elección y va sumando las partidas ganadas o perdidas a cada jugador.
        if Pc == "Piedra" and Usuario == "Papel": 
            victorias_jugador += 1
            print(f"Victoria Jugador!!! Usted lleva {victorias_jugador} victorias")
        elif Pc == "Papel" and Usuario == "Tijeras":
            victorias_jugador += 1
            print(f"Victoria Jugador!!! Usted lleva {victorias_jugador} victorias")
        elif Pc == "Tijeras" and Usuario == "Piedra":
            victorias_jugador += 1
            print(f"Victoria Jugador!!! Usted lleva {victorias_jugador} victorias")
        if Pc == "Piedra" and Usuario == "Tijeras":
            victorias_pc += 1
            print(f"Victoria PC!!! La PC lleva {victorias_pc} victorias")
        elif Pc == "Tijeras" and Usuario == "Papel":
            victorias_pc += 1
            print(f"Victoria PC!!! La PC lleva {victorias_pc} victorias")
        elif Pc == "Papel" and Usuario == "Piedra":
            victorias_pc += 1
            print(f"Victoria PC!!! La PC lleva {victorias_pc} victorias")
        elif Pc == Usuario:
            print("Empate > no suma victorias <")

        # Verificacion de Contador de victorias para determinar si alguien gano o se sigue jugando
        if victorias_jugador == 3:
            print(' ')
            print("Usted Gana la partida")
            jugando = False
        if victorias_pc == 3:
            print(' ')
            print("Usted pierde la partida")
            jugando = False

    print(" ")
    print("\t\tPresiona enter para volver al menu...")
    k=input()     
