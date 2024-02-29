import random

# Se crea la función para crear la matriz que toma los argumentos filas y columnas
def crear_matriz(filas, columnas):
    numeros = [0, 1, 2, 3, 4, 55, 111]
    
    # Inicializamos la matriz como una lista de listas dononde una fila esta representenda por una lista con columnas y tenemos filas de estas listas
    matriz = [[0 for _ in range(columnas)] for _ in range(filas)]

    # Poner un 0 en la coordenada (0, 0)
    matriz[0][0] = 0

    # Elegir aleatoriamente la posición de los números 2, 3 y 4
    for num in [2, 3, 4]:
        # Se elige aleatoriamente un número de fila
        fila = random.randint(0, filas - 1)
        
        # Se elige aleatoriamente un número de columna
        columna = random.randint(0, columnas - 1)
        
        # Asegurarse de que la celda esté vacía
        while matriz[fila][columna] != 0: 
            
             # Si la celda no está vacía, se selecciona una nueva fila aleatoria 
            fila = random.randint(0, filas - 1)
            
            # Si la celda no está vacía, se selecciona una nueva columna aleatoria
            columna = random.randint(0, columnas - 1)
            
        # Cuando se encuentra una celda vacía se asigna el número (2, 3 o 4) a esa posición 
        matriz[fila][columna] = num

    # Rellenar el resto de la matriz con números aleatorios
    for i in range(filas):
        for j in range(columnas):
            # Si la celda está vacía y no es la (0, 0), elegir un número aleatorio
            if matriz[i][j] == 0 and (i, j) != (0, 0):  
                
                #Elige aleatoriamente uno de los en la lista numeros excepto los números 2, 3 y 4, y lo asigna a la celda
                matriz[i][j] = random.choice([num for num in numeros if num not in [2, 3, 4]])

    return matriz

# Ejemplo 
matriz = crear_matriz(8, 8)

# Imprimir la matriz
for fila in matriz:
    
    # Se inicializa una cadena vacia para que represente una fila de la matriz
    fila_str = ""
    
    # Se usa para procesar y mostrar correctamente cada celda y fila de la matriz cuando se imprime
    for celda in fila:
        # Usa 5 espacios por celda
        fila_str += "{:5}".format(celda)  
        
    print(fila_str)
