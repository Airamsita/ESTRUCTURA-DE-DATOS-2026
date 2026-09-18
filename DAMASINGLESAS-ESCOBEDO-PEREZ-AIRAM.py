# JUEGO DE DAMAS INGLESAS

# TABLERO etsa hecho con una lista para las posiciones
tablero = [
    [".", "O", ".", "O", ".", "O", ".", "O"],
    ["O", ".", "O", ".", "O", ".", "O", "."],
    [".", "O", ".", "O", ".", "O", ".", "O"],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    ["X", ".", "X", ".", "X", ".", "X", "."],
    [".", "X", ".", "X", ".", "X", ".", "X"],
    ["X", ".", "X", ".", "X", ".", "X", "."]
]

# MOSTRAR TABLERO
def mostrar_tablero():

    print()
    print("  0 1 2 3 4 5 6 7")

    for fila in range(8):
        print(fila, end=" ")

        for columna in range(8):
            print(tablero[fila][columna], end=" ")

        print()


# CONTAR FICHAS  se cuentan las fichas de cada jugador con ayuda de un ciclo for
def contar_fichas(jugador):

    cantidad = 0

    for fila in range(8):
        for columna in range(8):

            if tablero[fila][columna] == jugador:
                cantidad = cantidad + 1

    return cantidad


# MOVER FICHA se selecciona donde esta ubicada la ficha y verifica si es del jugador
def mover_ficha(jugador):

    print("Turno del jugador", jugador)

    fila = int(input("Fila de la ficha: "))
    columna = int(input("Columna de la ficha: "))

    nueva_fila = int(input("Nueva fila: "))
    nueva_columna = int(input("Nueva columna: "))

    # Comprobar que la ficha sea del jugador
    if tablero[fila][columna] != jugador:
        print("Esa ficha no es tuya.")
        return False

    # Comprobar que la casilla nueva esté vacía
    if tablero[nueva_fila][nueva_columna] != ".":
        print("La casilla está ocupada.")
        return False

    # Calcular cuánto se movió
    movimiento_fila = nueva_fila - fila
    movimiento_columna = nueva_columna - columna

    # MOVIMIENTO NORMAL
    if abs(movimiento_fila) == 1 and abs(movimiento_columna) == 1:

        tablero[nueva_fila][nueva_columna] = jugador
        tablero[fila][columna] = "."

        return True


    # CAPTURAR UNA FICHA
    if abs(movimiento_fila) == 2 and abs(movimiento_columna) == 2:

        # Encontrar la casilla que está en medio
        fila_medio = (fila + nueva_fila) // 2
        columna_medio = (columna + nueva_columna) // 2

        # Saber cuál es el jugador contrario
        if jugador == "X":
            enemigo = "O"
        else:
            enemigo = "X"

        # Comprobar si hay una ficha enemiga
        if tablero[fila_medio][columna_medio] == enemigo:

            tablero[nueva_fila][nueva_columna] = jugador
            tablero[fila][columna] = "."

            # Eliminar la ficha capturada
            tablero[fila_medio][columna_medio] = "."

            print("¡Capturaste una ficha!")

            return True

    print("Movimiento no válido.")

    return False

jugador = "X"

while True:

    mostrar_tablero()

    # Comprobar si algún jugador perdió todas sus fichas
    if contar_fichas("X") == 0:
        print("¡Ganó el jugador O!")
        break

    if contar_fichas("O") == 0:
        print("¡Ganó el jugador X!")
        break

    movimiento = mover_ficha(jugador)

    # Cambiar turno
    if movimiento == True:

        if jugador == "X":
            jugador = "O"
        else:
            jugador = "X"