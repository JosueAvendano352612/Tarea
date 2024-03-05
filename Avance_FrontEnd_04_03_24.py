import pygame
import random

# Dimensiones del laberinto
filas = 10
columnas = 10
ancho_celda = 30

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)

# Crear laberinto
def crear_laberinto():
    laberinto = [[1 for _ in range(columnas)] for _ in range(filas)]
    # Posición inicial
    laberinto[0][0] = 0
    visitados = set()
    visitados.add((0, 0))
    # Celdas que pueden ser vecinas
    vecinos = [(0, 1), (1, 0)]
    while visitados:
        fila, columna = visitados.pop()
        random.shuffle(vecinos)
        for dx, dy in vecinos:
            nx, ny = fila + dx, columna + dy
            if 0 <= nx < filas and 0 <= ny < columnas and laberinto[nx][ny] == 1:
                laberinto[nx][ny] = 0
                visitados.add((nx, ny))
                laberinto[fila + dx // 2][columna + dy // 2] = 0
                break
    # Posicionar salida
    laberinto[filas - 1][columnas - 1] = 2

    return laberinto

# Función para dibujar el laberinto
def dibujar_laberinto(laberinto):
    for i in range(filas):
        for j in range(columnas):
            if laberinto[i][j] == 1:
                pygame.draw.rect(ventana, NEGRO, (j * ancho_celda, i * ancho_celda, ancho_celda, ancho_celda))
            elif laberinto[i][j] == 2:
                pygame.draw.rect(ventana, ROJO, (j * ancho_celda, i * ancho_celda, ancho_celda, ancho_celda))
            elif laberinto[i][j] == 0:
                pygame.draw.rect(ventana, BLANCO, (j * ancho_celda, i * ancho_celda, ancho_celda, ancho_celda))

# Función para mover al jugador
def mover_jugador(dx, dy):
    global jugador_fila, jugador_columna
    nueva_fila = jugador_fila + dx
    nueva_columna = jugador_columna + dy
    if 0 <= nueva_fila < filas and 0 <= nueva_columna < columnas and laberinto[nueva_fila][nueva_columna] != 1:
        jugador_fila = nueva_fila
        jugador_columna = nueva_columna

# Iniciar pygame
pygame.init()

# Configurar ventana
ancho_ventana = columnas * ancho_celda
alto_ventana = filas * ancho_celda
ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))
pygame.display.set_caption("Laberinto")

# Crear laberinto
laberinto = crear_laberinto()

# Posición inicial del jugador
jugador_fila = 0
jugador_columna = 0

# Bucle principal
jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                mover_jugador(-1, 0)
            elif event.key == pygame.K_DOWN:
                mover_jugador(1, 0)
            elif event.key == pygame.K_LEFT:
                mover_jugador(0, -1)
            elif event.key == pygame.K_RIGHT:
                mover_jugador(0, 1)

    ventana.fill(BLANCO)
    dibujar_laberinto(laberinto)
    pygame.draw.rect(ventana, VERDE, (jugador_columna * ancho_celda, jugador_fila * ancho_celda, ancho_celda, ancho_celda))
    pygame.display.update()

pygame.quit()
