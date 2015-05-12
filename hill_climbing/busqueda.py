from queens import *

dim = 10

t = Tablero(dim)
inicializaTableroAleatorio(t)
actual = t

while(actual.coste() != 0):
	costeActual = actual.coste()
	nuevo = None
	
	hijos = generaHijosTablero(t)
	
	for h in hijos:
		if h.coste() < costeActual:
			nuevo = h
			
	if nuevo is None: #No se mejoró el coste actual
		#print("Atascado en coste " + str(costeActual))
		nuevo = Tablero(dim)
		inicializaTableroAleatorio(nuevo)
		
	actual = nuevo

if actual.coste() == 0:
	print("Solución encontrada!")
	actual.imprimir()
