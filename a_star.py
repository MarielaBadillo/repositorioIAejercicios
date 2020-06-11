
import queue

laberinto =[["#","#","#","*","#","#","#","#"],
			["#"," "," "," "," "," "," ","#"],
			["#"," ","#"," ","#","#"," ","#"],
			["#"," ","#"," "," "," "," ","#"],
			["#"," ","#"," ","#","#"," ","#"],
			["#"," ","#","#","#","#"," ","#"],
			["#"," "," "," "," "," ","~","#"],
			["#","#","#","#","#","#","#","#"]]

#L izquierda
#R derecha
#D abajo
#U arriba

def ruta(laberinto, path=""):
	for x, pos in enumerate(laberinto[0]):
		if pos == "*":
			inicio = x
	x = inicio
	y = 0
	pos = set()
	for mov in path:
		if mov == "L":
			x -= 1
		elif mov == "R":
			x += 1
		elif mov == "U":
			y += 1
		elif mov == "D":
			y -= 1
		pos.add((y, x))

	for y, fila in enumerate(laberinto):
		for x, col in enumerate(fila):
			if (y, x) in pos:
				print("+ ", end="")
			else:
				print(col + " ", end="")
		print()
def validar(laberinto, movimientos):
	for x, pos in enumerate(laberinto[0]):
		if pos == "*":
			inicio = x
	x = inicio
	y = 0
	for mov in movimientos:
		if mov == "L":
			x -= 1
		elif mov == "R":
			x += 1
		elif mov == "U":
			y += 1
		elif mov == "D":
			y -= 1
		if not(0 <= x < len(laberinto[0]) and 0 <= y < len(laberinto)):
			return False
		elif (laberinto[y][x] == "#"):
			return False
	return True
def fin(laberinto, movimientos):
	for x, pos in enumerate(laberinto[0]):
		if pos == "*":
			start = x
	x = start
	y = 0
	for mov in movimientos:
		if mov == "L":
			x -= 1
		elif mov == "R":
			x += 1
		elif mov == "U":
			y += 1
		elif mov == "D":
			y -= 1
	if laberinto[y][x] == "~":
		print("Ruta a seguir " + movimientos)
		ruta(laberinto, movimientos)
		return True
	return False

x = queue.Queue()
x.put("")
add = ""

while not fin(laberinto, add): 
	add = x.get()
	for j in ["L ", "R ", "U ", "D "]:
		put = add + j
		if validar(laberinto, put):
			x.put(put)
