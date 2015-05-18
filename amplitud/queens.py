from random import shuffle

class Tablero:

	def __init__(self, dim):
		self.dimensiones = dim #Dimensiones del tablero (no. de reinas/fil/col)
		self.reinas = [] #Lista de reinas (tuplas fila/columna)
		self.costeCalculado = None

	def copy(self):
		t = Tablero(self.dimensiones)
		t.reinas = self.reinas.copy()
		return t

	def coste(self):
		if self.costeCalculado is None:
			self.costeCalculado = 0
			for rA in range(len(self.reinas)):
				for rB in range(rA+1, len(self.reinas)):
					if seAtacan(self.reinas[rA],self.reinas[rB]): self.costeCalculado = self.costeCalculado+1

		return self.costeCalculado

	#Imprime por pantalla el tablero
	def imprimir(self):
		CASILLA_REINA = "Q"
		CASILLA_VACIA = "*"

		for i in range(self.dimensiones):
			linea = ""
			for j in range(self.dimensiones):
				if (i,j) in self.reinas:
					linea += CASILLA_REINA
				else:
					linea += CASILLA_VACIA

			#Añade un espacio entre cada casilla
			linea = ' '.join(linea)
			print(linea)

	#Comparación (menor que) para poder ordenar por coste
	def __lt__(self, other):
		return self.coste() < other.coste()



def inicializaTableroAleatorio(tab):
	del tab.reinas[:] #Vacía el tablero

	#Crea una lista con los valores de 0 hasta dim-1
	#Estos serán los valores de las columnas
	col = [i for i in range(tab.dimensiones)]

	#Desordena los valores aleatoriamente
	shuffle(col)

	#Añade las tuplas como posiciones de las reinas en el tablero
	for fil in range(tab.dimensiones):
		tab.reinas.append( (fil, col[fil]) )

	tab.coste()

#Genera todos los tableros hijos del tablero dado
#devuelve una lista de tableros
def generaHijosTablero(tab):
	hijos = []

	for i in range(tab.dimensiones):
		for j in range(tab.dimensiones):
			#Para todas las columnas distintas a la que ya es igual
			if j != tab.reinas[i][1]:
				nuevo = tab.copy()
				nuevo.reinas[i] = (i,j)
				hijos.append(nuevo)

	return hijos

#Indica si dos reinas se atacan
def seAtacan(r1, r2):
	#Hay que tener en cuenta que es imposible que se
	#ataquen por filas debido a que el número de la fila
	#nunca cambia durante la ejecución
	if r1[1] == r2[1]:
		return True
	else:
		delta_fil = abs(r1[0] - r2[0])
		delta_col = abs(r1[1] - r2[1])

		if	delta_fil == delta_col:
			return True
		else:
			return False
