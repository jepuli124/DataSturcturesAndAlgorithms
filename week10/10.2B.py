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


graph = Graph(6)
connections = ((0, 2, 7), (0, 4, 9), (2, 1, 5),
                (2, 3, 1), (2, 5, 2), (3, 0, 6),
                (3, 5, 2), (4, 5, 1), (5, 1, 6))
for u, v, w in connections:
    graph.add(u, v, w)

M = graph.all_paths()
for weights in M:
    for weight in weights:
        print(f"{weight:3d}", end="")
    print()
#  0 12  7  8  9  9
# -1  0 -1 -1 -1 -1
#  7  5  0  1 16  2
#  6  8 13  0 15  2
# -1  7 -1 -1  0  1
# -1  6 -1 -1 -1  0