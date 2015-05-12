from queens import *

dim = 10

t = Tablero(dim)
frontera = [t]
explorados = []

while frontera: #Mientras exista algún elemento en frontera
	#Extrae el estado de menor coste de frontera
	actual = frontera.pop(frontera.index(min(frontera)))
	
	if actual.coste() == 0: #Esto significa que lo ha encontrado
		break
	
	#Lo añade a explorados
	explorados.append(actual)
	
	hijos = generaHijosTablero(actual)
	
	#Lo siguiente se encuentra comentado ya que el
	#not in se convierte en una operación costosa
	#De todas formas, como siempre se escoge el elemento
	#de frontera de menor coste, es muy dificil explorar el
	#mismo estado dos veces
	
#	for h in hijos:
#		if h not in explorados:
	frontera.extend(hijos)

if actual.coste() == 0:
	print("Solución encontrada!")
	actual.imprimir()
