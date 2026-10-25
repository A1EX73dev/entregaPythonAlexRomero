import random

def mostrarMenu():
    while True:
        print('******* MENÚ JUEGOS *******')
        print('1) Jugar a PIEDRA, PAPEL, TIJERA. ')
        print('2) Jugar al AHORCADO. ')
        print('3) Jugar al TRES EN RAYA. ')
        print('4) Jugar al BLACKJACK')
        print('5) Salir.')

        opMenu = int(input('Introduce la opción a ejecutar: '))
        match opMenu:
            case 1:
                jugarPPT()
            case 2:
                jugarAhorcado()
            case 3:
                jugar3R()
            case 4:
                #jugarBJ()
                print('Juego en desarrollo. No disponible.')
            case 5: 
                print('Saliendo del programa. Hasta la próxima!')
                break


def jugarPPT():
    print('Bienvenido al Piedra, Papel o Tijera.')
    print('Para lanzar Piedra pulsa 1.')
    print('Para lanzar Papel pulsa 2.')
    print('Para lanzar Tijera pulsa 3.')
    print('Para Salir pulsa 4.')

    vicJ1 = 0
    vicNPC = 0
    victoriasNecesarias = 3
    while vicJ1 != victoriasNecesarias and vicNPC != victoriasNecesarias:
        opJugada = int(input('Introduce tu jugada: '))
        #opciones npc: piedra = 0, papel = 1, tijera = 2
        opNPC = random.randint(0,2)
        if opJugada-1 == opNPC:
            print('Ronda empatada.')
        elif opJugada == 1 and opNPC != 1 or opJugada == 2 and opNPC != 2 or opJugada == 3 and opNPC != 0:
            print('Ronda ganada!')
            vicJ1 += 1
        else:
            print('Ronda perdida!')
            vicNPC += 1

    if vicJ1 == 3:
        print('Enorabuena has ganado la partida!')
    elif vicNPC == 3:
        print('Lástima, has perdido la partida. Vuelve a intentar... Ánimo!')



def jugarAhorcado():
    palabras = ['casa', 'perro', 'gato', 'sol', 'luna', 'mesa', 'silla', 'libro', 'raton', 'arbol',
                'playa', 'nube', 'fuego', 'agua', 'tren', 'coche', 'flor', 'queso', 'lapiz', 'puerta']

    palabra = random.choice(palabras)
    intentos = len(palabra) * 2
    tablero = ['_'] * len(palabra)
    letrasUsadas = []

    print('Bienvenido al Ahorcado.')
    print(f'La palabra tiene {len(palabra)} letras. Tienes {intentos} intentos.')

    while intentos > 0 and '_' in tablero:
        print()
        print(f'{" ".join(tablero)}')
        print(f'Intentos restantes: {intentos}')
        if len(letrasUsadas) > 0:
            print(f'Letras usadas: {", ".join(letrasUsadas)}')

        letra = input('Introduce una letra: ').lower()

        if len(letra) != 1 or not letra.isalpha():
            print('Debes introducir una sola letra.')
        elif letra in letrasUsadas:
            print('Ya has probado esa letra.')
        else:
            letrasUsadas.append(letra)
            intentos -= 1
            if letra in palabra:
                print('Bien! La letra está en la palabra.')
                for i in range(len(palabra)):
                    if palabra[i] == letra:
                        tablero[i] = letra.upper()
            else:
                print('La letra no está en la palabra.')

    print()
    print(f'{" ".join(tablero)}')
    if '_' not in tablero:
        print(f'Enhorabuena! Has adivinado la palabra: {palabra.upper()}')
    else:
        print(f'Te has quedado sin intentos. La palabra era: {palabra.upper()}')
    



def jugar3R():
    tablero = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    lineas = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    ficha = 'X'

    for turno in range(9):
        print(f"\n {tablero[0]} | {tablero[1]} | {tablero[2]}\n---+---+---\n {tablero[3]} | {tablero[4]} | {tablero[5]}\n---+---+---\n {tablero[6]} | {tablero[7]} | {tablero[8]}\n")

        casilla = int(input(f"Turno de {ficha}, elige casilla (1-9): ")) - 1

        while casilla < 0 or casilla > 8 or tablero[casilla] in ['X', 'O']:
            casilla = int(input("Casilla inválida u ocupada. Elige otra: ")) - 1

        tablero[casilla] = ficha

        for a, b, c in lineas:
            if tablero[a] == tablero[b] == tablero[c]:
                print(f"\n {tablero[0]} | {tablero[1]} | {tablero[2]}\n---+---+---\n {tablero[3]} | {tablero[4]} | {tablero[5]}\n---+---+---\n {tablero[6]} | {tablero[7]} | {tablero[8]}")
                print(f"¡Ha ganado {ficha}!")
                return

        ficha = 'O' if ficha == 'X' else 'X'

    print("¡Empate!")


mostrarMenu()