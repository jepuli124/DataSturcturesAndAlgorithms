class Vertex:
    def __init__(self, label):
        self.label = label
        self.edges = []
    def add(self, vertex, weight):
        if vertex not in self.edges:
            tuble = (vertex, weight)
            self.edges.append(tuble)
        else: 
            for x in range(len(self.edges)):
                if self.edges[x][0] == vertex:
                    self.edges[x][1] = weight
                    print(self.edges)
                    break
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
        if vertex1 >= len(self.listOfVertices):return
        if vertex2 >= len(self.listOfVertices):return
        self.listOfVertices[vertex1].add(vertex2, weight)
        self.listOfVertices[vertex2].add(vertex1, weight)
    def remove(self, vertex1, vertex2):
        if vertex1 >= len(self.listOfVertices):return
        if vertex2 >= len(self.listOfVertices):return
        self.listOfVertices[vertex1].remove(vertex2)
        self.listOfVertices[vertex2].remove(vertex1)
    
    def debug(self):
        for x in self.listOfVertices:
            print(x.edges)

    def shortest_path(self, start, end):
        path = self.shortestPathRecursive(start, end, [self.listOfVertices[start]])
        if path == None:
            print(-1)
            return None
        return path

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
    def pathLengthWithLabels(self, path):
        length = 0
        for vertex in range(len(path)-1):
            if self.listOfVertices[path[vertex]].findEdgeByConnection(self.listOfVertices[path[vertex+1]]) != None:
                length += self.listOfVertices[path[vertex]].findEdgeByConnection(self.listOfVertices[path[vertex+1]])
            else:
                print(self.listOfVertices[path[vertex]].edges, self.listOfVertices[path[vertex+1]].label, "couldn't find")
                return length
        return length
    
    def min_expense(self):
        listofnextVertex = [0]
        length = [0]
        self.min_expenseRecursive(listofnextVertex, length)
        return length[0]
        
    def min_expenseRecursive(self, tree, length):
        listOfPaths = []
        for start in tree:
            for vertex in self.listOfVertices[start].edges:
                if vertex[0] not in tree:
                    listOfPaths.append(self.shortest_path(start, vertex[0]))
        if len(listOfPaths) <= 0:
            return tree
        pathLengths = 10**8
        pathVariable = None
        
        for path in listOfPaths:
            variable = self.pathLength(path)
            if variable < pathLengths:
                pathVariable = path
                pathLengths = variable
        length[0] += pathLengths
        tree.append(pathVariable[-1].label)
        print(tree)
        self.min_expenseRecursive(tree, length)
        return tree 

        


    
# graph = Graph(6)
# edges = ((0, 2, 7), (0, 4, 9), (2, 1, 5),
#             (2, 3, 1), (2, 5, 2), (3, 0, 6),
#             (3, 5, 2), (4, 5, 1), (5, 1, 6))
# for u, v, w in edges:
#     graph.add(u, v, w)

# print(graph.min_expense())  # 15

# graph.remove(2, 3)

# print(graph.min_expense())  # 16

graph = Graph(6)

connections = (( 1,  2, 17), ( 4,  6, 14), ( 2,  5, 15),
               ( 3,  4,  3), ( 0,  5, 18), ( 3,  5,  8),
               ( 2,  0,  9), ( 0,  2, 19), ( 0,  1, 10),
               ( 1,  0, 13), ( 4,  1, 12), ( 5,  1,  3))

for u, v, w in connections:
    graph.add(u, v, w)

print(graph.min_expense())

graph.remove(3, 4)
graph.remove(1, 0)
graph.remove(4, 1)

print(graph.min_expense())