class Vertex:
    
    def __init__(self, label):
        self.label = label
        self.edges = []
        self.visited = False
    def add(self, vertex):
        if vertex not in self.edges:
            self.edges.append(vertex)
        self.edges.sort()
    def remove(self, vertex):
        for edge in range(len(self.edges)):
            if self.edges[edge] == vertex:
                self.edges.pop(edge)
                break
        self.edges.sort()
    

class Graph:
    listOfVertices = []
    def __init__(self, numberOfVertices):
        for x in range(numberOfVertices):
            self.listOfVertices.append(Vertex(x))
    def add(self, vertex1, vertex2):
        self.listOfVertices[vertex1].add(vertex2)
        self.listOfVertices[vertex2].add(vertex1)
    def remove(self, vertex1, vertex2):
        self.listOfVertices[vertex1].remove(vertex2)
        self.listOfVertices[vertex2].remove(vertex1)
    
    def dft(self, start):
        for vertex in self.listOfVertices:
            vertex.visited = False
        self.dftRecursive(self.listOfVertices[start])
        print("")

    def dftRecursive(self, vertex):
        if vertex != None and not vertex.visited:     
            print(vertex.label, end=" ")
            vertex.visited = True
        for newVertex in vertex.edges:
            if self.listOfVertices[newVertex].visited == False:
                self.dftRecursive(self.listOfVertices[newVertex])

    def bft(self, start):
        for vertex in self.listOfVertices:
            vertex.visited = False
        forwardList = []
        self.bftRecursive(self.listOfVertices[start], forwardList)
        print("")

    def bftRecursive(self, vertex, forwardList):
        if len(forwardList) >= 1:
            forwardList.pop(0)
        if vertex != None and not vertex.visited:     
            print(vertex.label, end=" ")
            vertex.visited = True
        nextInList = []
        for newVertex in vertex.edges:
            if self.listOfVertices[newVertex].visited == False:
                nextInList.append(self.listOfVertices[newVertex])
                forwardList.append(self.listOfVertices[newVertex])
        for next in nextInList:
            print(next.label, end=" ")
            next.visited = True
        for next in forwardList:
            self.bftRecursive(next, forwardList)

    def debug(self):
        for x in self.listOfVertices:
            print(x.edges)



    # Compute shortest path distances from s, store them in D
    # def Dijkstra(G, s, D):
    #     for i in range(G.nodeCount()):   # Initialize
    #         D[i] = INFINITY
    #     D[s] = 0
    #     for i in range(G.nodeCount()):   # Process the vertices
    #         v = minVertex(G, D)          # Find next-closest vertex
    #         G.setValue(v, VISITED)
    #         if D[v] == INFINITY:
    #             return   # Unreachable
    #         for w in G.neighbors(v):
    #             if D[w] > D[v] + G.weight(v, w):
    #                 D[w] = D[v] + G.weight(v, w)




# graph = Graph(6)
# edges = ((0, 2), (0, 4), (2, 1),
#             (2, 3), (2, 5), (3, 0),
#             (3, 5), (4, 5), (5, 1))
# for u, v in edges:
#     graph.add(u, v)
# #graph.debug()

# graph.dft(0)           # 0 2 1 5 3 4 
# graph.bft(0)           # 0 2 3 4 1 5 

# graph.remove(0, 2)
# graph.remove(2, 5)
# graph.remove(1, 4)

# #graph.debug()
# graph.dft(0)           # 0 3 2 1 5 4 
# graph.bft(0)           # 0 3 4 2 5 1

graph = Graph(8)

connections = ((0, 6), (0, 7), (1, 0),
               (1, 2), (2, 3), (3, 6),
               (4, 3), (5, 4), (5, 6), 
               (6, 1), (6, 2), (6, 7))

for u, v, in connections:
    graph.add(u, v)

# graph.dft(0)
graph.debug()
graph.bft(7)

# graph.remove(7, 0)
# graph.remove(5, 4)
# graph.remove(2, 1)

# graph.dft(0)
# graph.bft(7)