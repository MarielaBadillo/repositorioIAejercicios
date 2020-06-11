import json

JSONDATA = None
with open('base.json') as f:
	JSONDATA = json.load(f)

origen = input("Nombre de la carpeta donde se busca el archivo: ")
destino = input("Nombre del archivo: ")

ruta=[]
 
def buscar(inicio,valor):

    ruta.append(inicio)
 
    if inicio==valor:
        return valor
 
    for i,v in JSONDATA['carpetas'].items():
 
        if v==inicio:
 
            resultado=buscar(i,valor)
 
            if resultado:
                return resultado
 
    ruta.pop()

    return 0
 
resultado=buscar(origen,destino)

if resultado:
    print(ruta)
else:
    print("Archivo no encontrado")
