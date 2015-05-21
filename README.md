# IA - N-Reinas

Distintos acercamientos al problema de las n-reinas, con el propósito de aprender sobre Inteligencia Artificial

Métodos implementados:
* Hill Climbing (escalada): Buscar siempre un hijo que mejore el coste inicial, si no se encuentra se empieza en un nuevo punto aleatorio
* Profundidad (v1): Mantiene un conjunto de estados explorados y frontera. Toma el de menor coste de frontera y genera sus hijos. Si éstos no estan explorados los añade a frontera. Repite hasta que el estado que toma es de coste 0.
* Profundidad (v2, paso a paso): Comienza con un tablero vacío y va añadiendo posibles reinas (en casillas no amenazadas) hasta que consigue posicionar las n reinas

Hasta ahora, el algoritmo más eficiente y que mejor escala parece ser Profundidad (v1)
