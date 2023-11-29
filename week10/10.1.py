class Vertex:
    def __init__(self, label):
        self.label = label
        self.visited = False
        self.edges = []
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
        for x in range(numberOfVertices): self.listOfVertices.append(Vertex(x))
    def add(self, vertex1, vertex2):
        self.listOfVertices[vertex1].add(vertex2)
        self.listOfVertices[vertex2].add(vertex1)
    def remove(self, vertex1, vertex2):
        self.listOfVertices[vertex1].remove(vertex2)
        self.listOfVertices[vertex2].remove(vertex1)

    def subgraphs(self):
        amount = 0
        for vertex in self.listOfVertices:
            vertex.visited = False
        for vertex in self.listOfVertices:
            if not vertex.visited:
                self.dftNoPrint(vertex.label)
                amount += 1
        return amount

    def dftNoPrint(self, start):
        self.dftRecursiveNoPrint(self.listOfVertices[start])

    def dftRecursiveNoPrint(self, vertex):
        if vertex != None and not vertex.visited:     
            vertex.visited = True
        for newVertex in vertex.edges:
            if self.listOfVertices[newVertex].visited == False:
                self.dftRecursiveNoPrint(self.listOfVertices[newVertex])
    
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

graph = Graph(6)
connections = ((0, 4), (2, 1),
                (2, 5), (3, 0),
                (5, 1))
for u, v in connections:
    graph.add(u, v)

print(graph.subgraphs())  # 2

more_connections = ((0, 2), (2, 3),
                    (3, 5), (4, 5))
for u, v in more_connections:
    graph.add(u, v)

print(graph.subgraphs())  # 1