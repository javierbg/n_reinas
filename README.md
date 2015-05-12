# IA - N-Reinas

Distintos acercamientos al problema de las n-reinas, con el propósito de aprender sobre Inteligencia Artificial

Métodos implementados:
* Hill Climbing (escalada): Buscar siempre un hijo que mejore el coste inicial, si no se encuentra se empieza en un nuevo punto aleatorio
* Amplitud: Mantiene un conjunto de estados explorados y frontera. Toma el de menor coste de frontera y genera sus hijos. Si éstos no estan explorados los añade a frontera. Repite hasta que el estado que toma es de coste 0.
