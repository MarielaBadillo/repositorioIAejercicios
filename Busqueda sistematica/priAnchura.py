import json

JSONDATA = None
with open('base.json') as f:
	JSONDATA = json.load(f)
	
origen = input("Nombre de la carpeta donde se busca el archivo: ")
destino = input("Nombre del archivo: ")


ruta=[]
 
fifo=[]
 
def buscar(inicio,valor,iteraciones):

    ruta.append(inicio)
 
    if inicio==valor:
        return (True,iteraciones)
 
    fifoAdd(inicio)
 
    if len(fifo)==0:
        return (False,iteraciones)
 
    return buscar(fifo.pop(0),valor,iteraciones+1)
 
def fifoAdd(inicio):

    for i,v in JSONDATA['carpetas'].items():
        if v==inicio:
            fifo.append(i)
 
resultado,iteraciones=buscar(origen,destino,1)
if resultado:
    print("Ha encontrado el archivo en {} iteraciones".format(iteraciones))
else:
    print("Archivo no encontrado")
print("El camino que ha realizado ha sido: {}".format(ruta))

