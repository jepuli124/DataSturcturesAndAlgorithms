class Vertex:
    def __init__(self, label):
        self.label = label
        self.edges = []
    def add(self, vertex, weight):
        if vertex not in self.edges:
            tuble = (vertex, weight)
            self.edges.append(tuble)
        self.sortListByDuble(self.edges)
    def remove(self, vertex):
        for edge in range(len(self.edges)):
            if self.edges[edge][0] == vertex:
                self.edges.pop(edge)
                break
        self.sortListByDuble(self.edges)
    def sortListByDuble(self, list): # I know this is copied from previous exercises
        #list.sort(key=lambda x: x[0])
        for cell in range(0, len(list)-1):
            j = cell-1
            while (j >= 0) and (list[j][0] > list[j+1][0]):
                S1 = list[j]
                S2 = list[j+1]
                list[j] = S2
                list[j+1] = S1
                j -= 1
        return list
    def findEdgeByConnection(self, destination):
        for edge in range(len(self.edges)):
            if self.edges[edge][0] == destination.label:
                return self.edges[edge][1]
    

class Graph:
    listOfVertices = []
    def __init__(self, numberOfVertices):
        for x in range(numberOfVertices):
            self.listOfVertices.append(Vertex(x))
    def add(self, vertex1, vertex2, weight):
        if vertex1 >= len(self.listOfVertices):return
        if vertex2 >= len(self.listOfVertices):return
        self.listOfVertices[vertex1].add(vertex2, weight)
    def remove(self, vertex1, vertex2):
        if vertex1 >= len(self.listOfVertices):return
        if vertex2 >= len(self.listOfVertices):return
        self.listOfVertices[vertex1].remove(vertex2)
        #self.listOfVertices[vertex2].remove(vertex1)
    
    def debug(self):
        for x in self.listOfVertices:
            print(x.edges)

    def shortest_path(self, start, end):
        
        path = self.shortestPathRecursive(start, end, [self.listOfVertices[start]])
        #print(path)
        if path == None:
            #print(-1)
            return -1
        # for vertexAlong in path:
        #     print(vertexAlong.label, end=" ")
        # print("")
        return self.pathLength(path)

    def shortestPathRecursive(self, vertex, end, path):
        if len(self.listOfVertices) <= vertex:
            return None
        if self.listOfVertices[vertex] in path and len(path) != 1:
            return None
        if path[-1] != self.listOfVertices[vertex]:
            path.append(self.listOfVertices[vertex])
        if vertex == end:
            return path.copy()
        listOfPaths = []
        for edge in self.listOfVertices[vertex].edges:
            if edge[0] not in path:
                listOfPaths.append(self.shortestPathRecursive(edge[0], end, path.copy()))
                if listOfPaths[-1] == None:
                    listOfPaths.pop(len(listOfPaths)-1)
        returnPath = []
        returnPathLength = -1
        for xPath in listOfPaths:
            if self.pathLength(xPath) < returnPathLength or returnPathLength == -1:
                returnPath = xPath.copy()
                returnPathLength = self.pathLength(xPath)
        if len(returnPath) > 0 and returnPath[-1].label == end:
            return returnPath.copy()
        else:
            return None
        
    def pathLength(self, path):
        length = 0
        for vertex in range(len(path)-1):
            if path[vertex].findEdgeByConnection(path[vertex+1]) != None:

                length += path[vertex].findEdgeByConnection(path[vertex+1])
            else:
                #print(path[vertex].edges, path[vertex+1].label, "couldn't find")
                return 10**8
        return length
    def all_paths(self):
        paths = []
        for vertex in self.listOfVertices:
            path = []
            for vertex2 in self.listOfVertices:
                path.append(self.shortest_path(vertex.label, vertex2.label))
            paths.append(path)
        return paths
    # def Floyd(self):
    #     D = []
    #     for i in range(len(self.listOfVertices)): 
    #         for j in range(len(self.listOfVertices)):
    #             if self.weight(i, j) != 0:
    #                 D[i][j] = self.weight(i, j)
    #     for k in range(G.n()):  # Compute all k paths
    #         for i in range(G.n()):
    #             for j in range(G.n()):
    #                 if (D[i][k] != float('inf') and
    #                     D[k][j] != float('inf') and
    #                     D[i][j] > D[i][k] + D[k][j]
    #                     ):
    #                     D[i][j] = D[i][k] + D[k][j]
    

# graph = Graph(6)
# connections = ((0, 2, 7), (0, 4, 9), (2, 1, 5),
#                 (2, 3, 1), (2, 5, 2), (3, 0, 6),
#                 (3, 5, 2), (4, 5, 1), (5, 1, 6))
# for u, v, w in connections:
#     graph.add(u, v, w)

# M = graph.all_paths()
# for weights in M:
#     for weight in weights:
#         print(f"{weight:3d}", end="")
#     print()
#  0 12  7  8  9  9
# -1  0 -1 -1 -1 -1
#  7  5  0  1 16  2
#  6  8 13  0 15  2
# -1  7 -1 -1  0  1
# -1  6 -1 -1 -1  0

graph = Graph(6)

connections = (( 1,  2, 17), ( 4,  6, 14), ( 2,  5, 15),
               ( 3,  4,  3), ( 0,  5, 18), ( 3,  5,  8),
               ( 2,  0,  9), ( 0,  2, 19), ( 0,  1, 10),
               ( 1,  0, 13), ( 4,  1, 12), ( 5,  1,  3))

for u, v, w in connections:
    graph.add(u, v, w)

A = graph.all_paths()

for row in A:
    print(row)

print()
graph.remove(3, 4)
graph.remove(1, 0)
graph.remove(4, 1)

A = graph.all_paths()
for row in A:
    print(row)

# Number of vertices:  40
# Add:  25 31 21
# Add:  35 28 15
# Add:  0 23 74
# Add:  3 30 45
# Add:  18 11 22
# Add:  15 25 99
# Add:  16 33 90
# Add:  6 16 30
# Add:  27 14 42
# Add:  12 24 86
# Add:  14 37 83
# Add:  12 28 36
# Add:  19 6 69
# Add:  0 16 37
# Add:  19 32 25
# Add:  30 18 36
# Add:  1 35 39
# Add:  31 4 28
# Add:  33 8 51
# Add:  31 30 29
# Add:  22 33 64
# Add:  28 5 28
# Add:  26 30 44
# Add:  8 15 24
# Add:  30 28 99
# Add:  25 18 30
# Add:  5 33 23
# Add:  13 3 67
# Add:  0 33 55
# Add:  33 1 52
# Add:  35 15 11
# Add:  18 16 76
# Add:  28 8 83
# Add:  26 30 68
# Add:  21 24 73
# Add:  7 15 95
# Add:  27 36 13
# Add:  17 6 56
# Add:  15 20 99
# Add:  11 22 78
# Add:  38 18 79
# Add:  38 20 29
# Add:  4 1 79
# Add:  26 7 12
# Add:  3 21 67
# Add:  16 37 42
# Add:  34 4 82
# Add:  1 28 88
# Add:  32 33 38
# Add:  34 32 28
# Add:  23 8 77
# Add:  17 5 96
# Add:  13 24 32
# Add:  10 11 56
# Add:  36 6 80
# Add:  2 39 56
# Add:  0 37 67
# Add:  24 13 24
# Add:  14 12 78
# Add:  12 10 69
# >>> >>> >>> None
# Remove: 29 27
# Remove: 5 24
# Remove: 7 14
# Remove: 0 37
# Remove: 32 33
# Remove: 6 16
# Remove: 16 37
# Remove: 31 30
# Remove: 13 3
# Remove: 22 37
# Remove: 38 20
# Remove: 23 28
# Remove: 5 33
# Remove: 16 25
# Remove: 33 17
# Remove: 12 10
# Remove: 12 24
# Remove: 11 8
# Remove: 9 15
# Remove: 24 4