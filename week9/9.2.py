
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
        self.listOfVertices[vertex1].add(vertex2, weight)
    def remove(self, vertex1, vertex2):
        self.listOfVertices[vertex1].remove(vertex2)
        #self.listOfVertices[vertex2].remove(vertex1)
    
    def debug(self):
        for x in self.listOfVertices:
            print(x.edges)

    def shortest_path(self, start, end):
        
        path = self.shortestPathRecursive(start, end, [self.listOfVertices[start]])
        #print(path)
        if path == None:
            print(-1)
            return
        for vertexAlong in path:
            print(vertexAlong.label, end=" ")
        print("")

    def shortestPathRecursive(self, vertex, end, path):
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
                print(path[vertex].edges, path[vertex+1].label, "couldn't find")
                return 10**10
        return length


    # def dft(self, start):
    #     for vertex in self.listOfVertices:
    #         vertex.visited = False
    #     self.dftRecursive(self.listOfVertices[start])
    #     print("")

    # def dftRecursive(self, vertex):
    #     if vertex != None and not vertex.visited:     
    #         print(vertex.label, end=" ")
    #         vertex.visited = True
    #     for newVertex in vertex.edges:
    #         if self.listOfVertices[newVertex].visited == False:
    #             self.dftRecursive(self.listOfVertices[newVertex])

    # def bft(self, start):
    #     for vertex in self.listOfVertices:
    #         vertex.visited = False
    #     forwardList = []
    #     self.bftRecursive(self.listOfVertices[start], forwardList)
    #     print("")

    # def bftRecursive(self, vertex, forwardList):
    #     if len(forwardList) >= 1:
    #         forwardList.pop(0)
    #     if vertex != None and not vertex.visited:     
    #         print(vertex.label, end=" ")
    #         vertex.visited = True
    #     nextInList = []
    #     for newVertex in vertex.edges:
    #         if self.listOfVertices[newVertex].visited == False:
    #             nextInList.append(self.listOfVertices[newVertex])
    #             forwardList.append(self.listOfVertices[newVertex])
    #     for next in nextInList:
    #         print(next.label, end=" ")
    #         next.visited = True
    #     for next in forwardList:
    #         self.bftRecursive(next, forwardList)



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

# graph = Graph(10)
# edges = ((0, 1, 25), (0, 2,  6), (1, 3, 10),
#             (1, 4,  3), (2, 3,  7), (2, 5, 25),
#             (3, 4, 12), (3, 5, 15), (3, 6,  4),
#             (3, 7, 15), (3, 8, 20), (4, 7,  2),
#             (5, 8,  2), (6, 7,  8), (6, 8, 13),
#             (6, 9, 15), (7, 9,  5), (8, 9,  1))
# for u, v, w in edges:
#     graph.add(u, v, w)
# graph.debug()
# graph.shortest_path(0, 9)   # 0 2 3 6 7 9
# graph.remove(3, 6)
# graph.remove(5, 6)
# graph.shortest_path(0, 9)   # 0 2 3 5 8 9

graph = Graph(6)

connections = ((0, 1, 24), (0, 2, 13),
               (1, 5,  9), (2, 5, 19),
               (3, 0, 25), (4, 0, 20),
               (5, 3, 18), (5, 4, 36))

for u, v, w in connections:
    graph.add(u, v, w)

graph.shortest_path(0, 3)
graph.shortest_path(3, 1)
graph.shortest_path(2, 4)

graph.remove(0, 2)
graph.remove(3, 0)

graph.shortest_path(0, 3)
graph.shortest_path(3, 1)
graph.shortest_path(2, 4)