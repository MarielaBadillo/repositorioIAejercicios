lista = [
	["A","B",1],
	["B","A",1],
	["A","Z",2],
	["Z","A",2],
	["Z","X",2],
	["X","Z",2],
	["X","Y",2],
	["Y","X",2],
	["Y","W",1],
	["W","Y",1],
	["W","R",1],
	["R","W",1],
	["R","T",2],
	["T","R",2],
	["T","Z",3],
	["Z","T",3],
	["W","U",2],
	["U","W",2],
	["U","V",3],
	["V","U",3],
	["V","H",3],
	["H","V",3],
	["H","I",1],
	["I","H",1],
	["G","H",2],
	["H","G",2],
	["S","G",3],
	["G","S",3],
	["S","V",2],
	["V","S",2],
	["R","S",1],
	["S","R",1],
	["S","E",4],
	["E","S",4],
	["F","E",2],
	["E","F",2],
	["G","F",3],
	["F","G",3],
	["E","D",1],
	["D","E",1],
	["C","D",2],
	["D","C",2],
	["C","B",1],
	["B","C",1],
	["D","B",2],
	["B","D",2]
]

from operator import itemgetter
import random


ruta = []



def buscar(inicio, fin):
	objetivo = 0
	anterior = ""
	while (objetivo == 0):
		mapa = [v for v in lista if (v[0] == inicio and v[1] != anterior)]
		menor = (min(mapa, key=itemgetter(2))[2])
		caminos = [c for c in mapa if (c[2] == menor and c[1] != anterior) ]
		if (len(caminos) > 1):
			actual = 0
			#evita recorrer un camino antiguo
			m = random.randint(0, len(caminos) -1)
			contador = 1
			while (actual == 0):
				valor = caminos[m]
			#evita que el nodo siguiente haya pasado en la ruta, tanto como inicio, como fin
				if (len([e for e in ruta if e[1] == valor[1]]) == 0 and len([e for e in ruta if e[0] == valor[1]]) == 0 ):
					actual = 1
				contador += 1
				
				if (contador > len(caminos)):
					actual = 1
					objetivo = 1
					print("Ruta ciclada, no se llego al objetivo")
		else:
			valor = caminos[0]
		ruta.append(valor)
		siguiente = valor[1]
		anterior = inicio

		if (siguiente == fin):
			objetivo = 1
		else:
			inicio = siguiente

buscar("Z","I")
print("Ruta desde Z hasta I")
print(ruta)
