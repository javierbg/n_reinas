from queens import *

dim = 20

t = Tablero(dim)
inicializaTableroAleatorio(t)
frontera = [t]
explorados = []
mejorCoste = t.coste()

while frontera: #Mientras exista algún elemento en frontera
	#Extrae el estado de menor coste de frontera
	actual = frontera.pop(frontera.index(min(frontera)))
	
	if actual.coste() == 0: #Esto significa que lo ha encontrado
		break
	
	#Lo añade a explorados
	explorados.append(actual)
	
	hijos = generaHijosTablero(actual)
	
	for h in hijos:
		if h not in explorados:
			frontera.append(h)

if actual.coste() == 0:
	print("Solución encontrada!")
	actual.imprimir()
	
else:
	print("No hay solución")
