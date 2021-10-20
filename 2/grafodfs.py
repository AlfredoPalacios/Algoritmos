class Grafo:
    adjacencia = []

    def __init__(self, v, a):
        self.v = v
        self.a = a
        Grafo.adjacencia = [[0 for i in range(v)]for j in range(v)]

    def agregarArista(self, inicio, a):
        Grafo.adjacencia[inicio][a] = 1
        Grafo.adjacencia[a][inicio] = 1

    def DFS(self, inicio, visitado):
        print(inicio, end = ' ')
        visitado[inicio] = True
        for i in range(self.v):
            if(Grafo.adjacencia[inicio][i] == 1 and (not visitado[i])):
                self.DFS(i, visitado)

v, a = 8, 8

Gfo = Grafo(v, a)
Gfo.agregarArista(0, 1)
Gfo.agregarArista(1, 2)
Gfo.agregarArista(2, 3)
Gfo.agregarArista(2, 4)
Gfo.agregarArista(3, 4)
Gfo.agregarArista(4, 5)
Gfo.agregarArista(0, 6)
Gfo.agregarArista(6, 7)

visitado = [False]*v

Gfo.DFS(0, visitado);