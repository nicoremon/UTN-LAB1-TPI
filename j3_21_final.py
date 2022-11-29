import random

def blackjack():

    palos = ["♥", "♠" ,"♦" , "♣"]
    rangos = [1,2,3,4,5,6,7,8,9,10,11]

    # definimos las dos primeras cartas del jugador solamente con el valor numerico aleatorio
    def carta_jugador():
        carta1=int(random.choice(rangos))
        carta2=int(random.choice(rangos))
        cartas(carta1,carta2)
        # si la carta es igual a 1 o a 11 le pregunta al jugador que valor quiere usar
        if carta1==1 or carta1==11:
           carta1 = valorAs()
        
        if carta2==1 or carta2==11:
            carta2 = valorAs()
        
        return carta1 + carta2

    # a las cartas del jugador se le agregan palos aleatorios
    def cartas(palo1,palo2):
        print('cartas jugador_: '+str(palo1) + random.choice(palos) +' '+ str(palo2) + random.choice(palos))
    # se crea la primera carta del dealer 
    def carta_dealer():
        carta1=int(random.choice(rangos))
        cartas_dealer(carta1)
        return carta1
    # se crea el palo al azar para la carta del dealer
    def cartas_dealer(palo1):
        print('cartas dealer: '+str(palo1) +random.choice(palos))

    def valorAs():
        while True:
            valorAs = 0
            valoresCorrectos = [1,11]
            try:
                valorAs = int(input("Que valor quiere que tenga la carta As, 1 o 11? "))
            except ValueError:
                print("Debes escribir el número 1 u 11.")
                continue

            if valorAs not in valoresCorrectos:
                print("Debes escribir el número 1 u 11.")
                continue
            else:
                break

        return valorAs

    # funcion para tirar carta cuando solicita el jugador
    def tirar_carta():
        num=int(random.choice(rangos))
        print("La nueva carta del jugador es: ", str(num)+random.choice(palos))
        if num == 1 or num == 11:
            num = valorAs()
            print("La nueva carta del jugador es: ", str(num)+random.choice(palos))
            print()
        return num

    # funcion para tirar carta dealer
    def tirar_cartadealer():
        num=int(random.choice(rangos))
        print("La nueva carta del dealer es: ", str(num)+random.choice(palos))
        print()
        return num
    
    # total de las cartas del jugador
    total_jugador = carta_jugador()
    print('total jugador:' + str(total_jugador))
    print()

    # total carta dealer
    total_dealer = carta_dealer()
    print('total dealer: ' + str(total_dealer))
    print()

    if total_jugador == 21:
        juego_jugador = False
        juego_dealer = True
    #mientras que el total del jugador sea menor a 21 pregunta si quiere otra carta
    juego_jugador = True
    juego_dealer = True
    while juego_jugador :
        comp=input(('Jugador, desea otra carta?Y/N:'))
        print()
        if comp=='Y' or comp=='y':
            total_jugador += tirar_carta()
            print("La suma de las cartas del Jugador es :", total_jugador)
            print()
            if total_jugador == 21:
                print("Gana el jugador")
                juego_jugador = False
                juego_dealer = False
            if total_jugador  > 21:
                print("El jugador se paso, gana la banca ")
                juego_jugador = False
                juego_dealer = False
        elif comp=='N' or comp=='n':
            juego_jugador = False

    while juego_dealer:
        while total_jugador > total_dealer and total_dealer<17:
            total_dealer+=tirar_cartadealer()
            print("La suma de las cartas del Dealer es: ", total_dealer)

        if total_dealer > total_jugador  and total_dealer <=21:
            print("Gana la banca")
            print()
            juego_jugador = False
            juego_dealer = False

        if total_dealer == 17 and total_dealer<total_jugador :
            print("La banca se planta")
            print()
            juego_jugador = False
            juego_dealer = False   

        if total_jugador > total_dealer and total_jugador <=21 :
            print("Gana el jugador ")
            print()
            juego_jugador = False
            juego_dealer = False

        if total_jugador  == total_dealer:
            print("Las cartas son iguales, Hay empate")
            print()
            juego_jugador = False
            juego_dealer = False

        elif total_dealer>21:
            print("La banca se paso, gana el Jugador")
            print()
            juego_jugador = False
            juego_dealer = False

    print(" ")
    jugar_de_nuevo = input("Quieres volver a Jugar ? (s/n): ")
    if jugar_de_nuevo == 's' or jugar_de_nuevo == 'S':
        blackjack()
    else:
        print(" ")        
        print("\t\tPresiona enter para volver al menu...")
        k=input()


