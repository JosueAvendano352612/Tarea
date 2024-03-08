import pygame
import random

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AMARILLO = (255, 255, 0)
AZUL = (0, 0, 255)
CIAN = (0,255,255)
def generar_laberinto(filas, columnas):
    laberinto = [[1 for _ in range(columnas)] for _ in range(filas)]

    # Inicializar el laberinto con todas las paredes
    for fila in range(filas):
        for columna in range(columnas):
            laberinto[fila][columna] = 1

    # Punto de partida
    laberinto[0][0] = 0
    fila_actual = 0
    columna_actual = 0

    # Pila para realizar backtracking
    pila = [(fila_actual, columna_actual)]

    while pila:
        vecinos = []

        # Buscar vecinos no visitados
        if fila_actual >= 2 and laberinto[fila_actual - 2][columna_actual] == 1:
            vecinos.append((-2, 0))
        if fila_actual <= filas - 3 and laberinto[fila_actual + 2][columna_actual] == 1:
            vecinos.append((2, 0))
        if columna_actual >= 2 and laberinto[fila_actual][columna_actual - 2] == 1:
            vecinos.append((0, -2))
        if columna_actual <= columnas - 3 and laberinto[fila_actual][columna_actual + 2] == 1:
            vecinos.append((0, 2))

        if vecinos:
            dx, dy = random.choice(vecinos)
            nueva_fila = fila_actual + dx
            nueva_columna = columna_actual + dy
            laberinto[nueva_fila][nueva_columna] = 0
            laberinto[fila_actual + dx // 2][columna_actual + dy // 2] = 0

            # Marcar celdas especiales con probabilidad de que salga
            if random.random() < 0.10:  # Probabilidad del 10% de que una celda sea una pregunta
                laberinto[nueva_fila][nueva_columna] = 111
            elif random.random() < 0.10:  # Probabilidad del 10% de que una celda sea una trivia
                laberinto[nueva_fila][nueva_columna] = 55
            elif random.random() < 0.10:  
                laberinto[nueva_fila][nueva_columna] = 3
            elif random.random() < 0.10:  
                laberinto[nueva_fila][nueva_columna] = 4
                
            pila.append((nueva_fila, nueva_columna))
            fila_actual = nueva_fila
            columna_actual = nueva_columna
        else:
            fila_actual, columna_actual = pila.pop()

    # Marcar la salida del laberinto en los bordes del laberinto
    salida_posible = [(0, random.randint(0, columnas - 1)), 
                    (filas - 1, random.randint(0, columnas - 1)), 
                    (random.randint(0, filas - 1), 0), 
                    (random.randint(0, filas - 1), columnas - 1)]
    salida = random.choice(salida_posible)
    laberinto[salida[0]][salida[1]] = 2

    return laberinto


def mover_jugador(dx, dy, laberinto, jugador_posicion):
    nueva_fila = jugador_posicion[0] + dx
    nueva_columna = jugador_posicion[1] + dy

    # Verificar si la nueva posición está dentro de los límites del laberinto y no es una pared
    if 0 <= nueva_fila < len(laberinto) and 0 <= nueva_columna < len(laberinto[0]) and laberinto[nueva_fila][nueva_columna] != 1:
        # Actualizar la posición del jugador
        jugador_posicion[0] = nueva_fila
        jugador_posicion[1] = nueva_columna

def main():
    # Dimensiones del laberinto
    filas = 20
    columnas = 20
    ancho_celda = 20

    # Iniciar pygame
    pygame.init()

    # Configurar ventana
    ancho_ventana = columnas * ancho_celda
    alto_ventana = filas * ancho_celda
    ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))
    pygame.display.set_caption("Laberinto")

    # Generar laberinto
    laberinto_personalizado = generar_laberinto(filas, columnas)

    # Posición inicial del jugador
    jugador_posicion = [0, 0]

    # Bucle principal
    jugando = True
    while jugando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jugando = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    mover_jugador(-1, 0, laberinto_personalizado, jugador_posicion)
                elif event.key == pygame.K_DOWN:
                    mover_jugador(1, 0, laberinto_personalizado, jugador_posicion)
                elif event.key == pygame.K_LEFT:
                    mover_jugador(0, -1, laberinto_personalizado, jugador_posicion)
                elif event.key == pygame.K_RIGHT:
                    mover_jugador(0, 1, laberinto_personalizado, jugador_posicion)

        ventana.fill(BLANCO)
        # Dibujar laberinto
        for i in range(filas):
            for j in range(columnas):
                if laberinto_personalizado[i][j] == 1:
                    pygame.draw.rect(ventana, NEGRO, (j * ancho_celda, i * ancho_celda, ancho_celda, ancho_celda))
                elif laberinto_personalizado[i][j] == 2:
                    pygame.draw.rect(ventana, ROJO, (j * ancho_celda, i * ancho_celda, ancho_celda, ancho_celda))
                elif laberinto_personalizado[i][j] == 0:
                    pygame.draw.rect(ventana, BLANCO, (j * ancho_celda, i * ancho_celda, ancho_celda, ancho_celda))
                elif laberinto_personalizado[i][j] == 111:  # Color para preguntas
                    pygame.draw.rect(ventana, AMARILLO, (j * ancho_celda, i * ancho_celda, ancho_celda, ancho_celda))
                elif laberinto_personalizado[i][j] == 55:  # Color para tribias
                    pygame.draw.rect(ventana, AMARILLO, (j * ancho_celda, i * ancho_celda, ancho_celda, ancho_celda))
                elif laberinto_personalizado[i][j] == 3:
                    pygame.draw.rect(ventana, AZUL, (j * ancho_celda, i * ancho_celda, ancho_celda, ancho_celda))
                elif laberinto_personalizado[i][j] == 4:
                    pygame.draw.rect(ventana, CIAN, (j * ancho_celda, i * ancho_celda, ancho_celda, ancho_celda))

        # Dibujar jugador
        pygame.draw.rect(ventana, VERDE, (jugador_posicion[1] * ancho_celda, jugador_posicion[0] * ancho_celda, ancho_celda, ancho_celda))

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
