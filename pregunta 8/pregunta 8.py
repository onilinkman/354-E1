import numpy as np

# Matriz de distancias
distancias = np.array([
    [0, 11.85, 6.15, 9.11, 3.13, 5.09, 3.35, 10.60, 7.62, 11.72],
    [11.85, 0, 9.22, 9.13, 11.93, 11.53, 10.86, 3.89, 10.34, 4.37],
    [6.15, 9.22, 0, 11.83, 8.62, 9.94, 3.03, 6.23, 11.29, 11.38],
    [9.11, 9.13, 11.83, 0, 6.77, 4.95, 10.93, 11.16, 2.08, 5.66],
    [3.13, 11.93, 8.62, 6.77, 0, 2.08, 6.24, 11.70, 4.94, 10.64],
    [5.09, 11.53, 9.94, 4.95, 2.08, 0, 7.92, 11.98, 2.97, 9.52],
    [3.35, 10.86, 3.03, 10.93, 6.24, 7.92, 0, 8.62, 9.91, 11.97],
    [10.60, 3.89, 6.23, 11.16, 11.70, 11.98, 8.62, 0, 11.76, 7.76],
    [7.62, 10.34, 11.29, 2.08, 4.94, 2.97, 9.91, 11.76, 0, 7.41],
    [11.72, 4.37, 11.38, 5.66, 10.64, 9.52, 11.97, 7.76, 7.41, 0]])

# Número de ciudades
num_ciudades = len(distancias)

# Población máxima de soluciones
tam_poblacion = 150

def calcular_distancia(recorrido):
    distancia_total = 0
    for i in range(num_ciudades - 1):
        ciudad_actual = recorrido[i]
        ciudad_siguiente = recorrido[i + 1]
        distancia_total += distancias[ciudad_actual][ciudad_siguiente]
    # Agregar la distancia de regreso a la ciudad inicial
    distancia_total += distancias[recorrido[-1]][recorrido[0]]
    return distancia_total

# Función para inicializar la población
def inicializar_poblacion(tam_poblacion, num_ciudades):
    poblacion = []
    while len(poblacion) < tam_poblacion:
        recorrido = list(np.random.permutation(range(1, num_ciudades))) # Generamos una permutación sin incluir el 0
        recorrido.insert(0, 0) # Agregamos el 0 al inicio del recorrido
        if recorrido not in poblacion: # Verificamos si la permutación no ha sido generada antes
            poblacion.append(recorrido)
    return poblacion

def evaluar_poblacion(poblacion):
    evaluaciones = []
    for recorrido in poblacion:
        distancia = calcular_distancia(recorrido)
        evaluaciones.append((recorrido, distancia))
    # Ordenar por distancia de menor a mayor
    evaluaciones.sort(key=lambda x: x[1])
    return evaluaciones

# Algoritmo principal
def algoritmo_genetico():
    poblacion = inicializar_poblacion(tam_poblacion, num_ciudades)
    distancias = evaluar_poblacion(poblacion)
    for j in range(len(poblacion)):
        print(j, distancias[j])

# Ejecutar el algoritmo genético
print("----------POBLACION----------")
algoritmo_genetico()