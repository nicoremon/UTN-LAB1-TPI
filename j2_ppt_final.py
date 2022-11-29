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
    jugando = True

    # Funcion para Solicitar numero al usuario y verificar si es valido
    def opcion():
        while True:
            opcion = 0
            numeros = [1,2,3]
            try:
                opcion = int(input("Ingresa la opcion: "))
            except ValueError:
                print("Debes escribir un número entre 1 y 3.")
                continue

            if opcion not in numeros:
                print("Debes escribir un número entre 1 y 3.")
                continue
            else:
                break

        return opcion

    # Elegir eleatorio -random- elegir jugador.
    while jugando:
        # En cada ciclo se genera una opcion aleatoria para la PC
        aleatorio = random.randint(1, 3)
        Pc = ""
        Usuario = ""

        # Se solicita al usuario que ingrese su eleccion verificando que sea valida (solo numeros del 1 al 3)
        eleccion = opcion()

        # Aqui comienza el recorrido de la eleccion del usuario
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
    jugar_de_nuevo = input("Quieres volver a Jugar ? (s/n): ")
    if jugar_de_nuevo == 's':
        ppt()
    else:
        print(" ")        
        print("\t\tPresiona enter para volver al menu...")
        k=input()    
