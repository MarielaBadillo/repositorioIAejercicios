global n 
n = 4 #Numero de reinas (4)

#Imprime la matriz con la solución
def solucion(matriz):
	for e in range(n):
		for f in range(n):
			print(matriz[e][f], end = ' ')
		print()

#Verifica si una reina se puede colocar
def verifica(matriz, fila, columna):
	for e in range(columna):
		if matriz[fila][e] == 1:
			return False
	for e, f in zip(range(fila, -1, -1), range(columna, -1, -1)):
		if matriz[e][f] == 1:
			return False
	for e, f in zip(range(fila, n, 1), range(columna, -1, -1)):
		if matriz[e][f] == 1:
			return False
	return True

#Solucion de nReinas
def solucionReinas(matriz, columna):
	if columna >= n:
		return True
	for e in range(n):
		if verifica(matriz, e, columna):
			matriz[e][columna] = 1
			if solucionReinas(matriz, columna + 1) == True:
				return True
			matriz[e][columna] = 0
	return False

def resuelveReinas():
	matriz = [ [0,0,0,0],
		    [0,0,0,0],
		    [0,0,0,0],
		    [0,0,0,0]
		]
	if solucionReinas(matriz, 0) == False:
		print("No hay solución")
		return False

	solucion(matriz)
	return True
resuelveReinas()

	