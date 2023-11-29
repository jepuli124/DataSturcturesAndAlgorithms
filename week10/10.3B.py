class Graph:
    def __init__(self, numberOfVertices):
        self.matrix = []
        for x in range(numberOfVertices):
            listOf0 = []
            for y in range(numberOfVertices):
                listOf0.append(0)
            self.matrix.append(listOf0)
    
    def add(self, x, y, weight):
        if x >= len(self.matrix) or y >= len(self.matrix):return
        self.matrix[x][y] = weight
    def remove(self, x, y):
        self.matrix[x][y] = 0

    def all_paths(self): #floyd from OpenDSA
        paths = []
        for x in range(len(self.matrix)):
            path = []
            for y in range(len(self.matrix)):
                path.append(-1)
            paths.append(path)
        for x in range(len(self.matrix)): 
            for y in range(len(self.matrix)):
                if self.matrix[x][y] != 0:
                    paths[x][y] = self.matrix[x][y]
        for x in range(len(self.matrix)):  
            for y in range(len(self.matrix)):
                for z in range(len(self.matrix)):
                    if y == z: paths[y][z] = 0
                    if (paths[y][x] != -1 and paths[x][z] != -1 and (paths[y][z] > paths[y][x] + paths[x][z] or paths[y][z] == -1)): paths[y][z] = paths[y][x] + paths[x][z]
        return paths
    
    def min_expense(self):
        
    def Prim(G, s, D, V): #Prim from openDSA
        for i in range(G.nodeCount()):  # Initialize
            D[i] = float('inf')
        D[s] = 0
        for i in range(G.nodeCount()):  # Process the vertices
            v = minVertex(G, D)         # Find next-closest vertex
            G.setValue(v, VISITED)
            if D[v] == float('inf'):
                return               
            if v != s:
                AddEdgetoMST(V[v], v)
            for w in G.neighbors(v):
                if D[w] > G.weight(v, w):
                    D[w] = G.weight(v, w)
                    V[w] = v

graph = Graph(6)
edges = ((0, 2, 7), (0, 4, 9), (2, 1, 5),
            (2, 3, 1), (2, 5, 2), (3, 0, 6),
            (3, 5, 2), (4, 5, 1), (5, 1, 6))
for u, v, w in edges:
    graph.add(u, v, w)

print(graph.min_expense())  # 15

graph.remove(2, 3)

print(graph.min_expense())  # 16