class Graph:
    def __init__(self, numberOfVertices):
        self.vertices = numberOfVertices
        self.edges = []
    def add(self, vertex1, vertex2, weight):
        if vertex1 >= self.vertices or vertex2 >= self.vertices:return
        for edge in range(len(self.edges)):
            if (self.edges[edge][0] == vertex1 and self.edges[edge][1]  == vertex2)or(self.edges[edge][1]  == vertex1 and self.edges[edge][0]  == vertex2):
                self.edges[edge][2] = weight

        self.edges.append([vertex1, vertex2, weight])
        self.edges.append([vertex2, vertex1, weight])
    def remove(self, vertex1, vertex2):
        for edge in range(len(self.edges)):
            if (self.edges[edge][0] == vertex1 and self.edges[edge][1]  == vertex2)or(self.edges[edge][1]  == vertex1 and self.edges[edge][0]  == vertex2):
                self.edges.pop(edge)
                self.remove(vertex1, vertex2)
                break
    def min_expense(self):
        listofnextVertex = [0]
        length = [0]
        value = []
        for x in range(self.vertices):
            if x not in value:
                listofnextVertex = [x]
                value.extend(self.min_expenseRecursive(listofnextVertex, length))
        
        return length[0]
        
    def min_expenseRecursive(self, tree, length):
        listOfPaths = []
        for vertex in tree:
            for edge in range(len(self.edges)):
                if (self.edges[edge][0] == vertex and self.edges[edge][1] not in tree)or (self.edges[edge][1] == vertex and self.edges[edge][0] not in tree):
                    listOfPaths.append(self.edges[edge])
        if len(listOfPaths) <= 0:
            return tree
        pathLengths = 10**8
        pathVariable = None
        
        for path in listOfPaths:
            variable = path[2]
            if variable < pathLengths:
                pathVariable = path
                pathLengths = variable
        #print(pathVariable)
        length[0] += pathLengths
        if pathVariable[0] in tree:
            tree.append(pathVariable[1])
        else:
            tree.append(pathVariable[0])
        #print(tree)
        self.min_expenseRecursive(tree, length)
        return tree 


# graph3 = Graph(6)
# edges = ((0, 2, 7), (0, 4, 9), (2, 1, 5),
#             (2, 3, 1), (2, 5, 2), (3, 0, 6),
#             (3, 5, 2), (4, 5, 1), (5, 1, 6))
# for u, v, w in edges:
#     graph3.add(u, v, w)

# print(graph3.min_expense())  # 15

# graph3.remove(2, 3)

# print(graph3.min_expense())  # 16

# graph2 = Graph(6)

# connections = (( 1,  2, 17), ( 4,  6, 14), ( 2,  5, 15),
#                ( 3,  4,  3), ( 0,  5, 18), ( 3,  5,  8),
#                ( 2,  0,  9), ( 0,  2, 19), ( 0,  1, 10),
#                ( 1,  0, 13), ( 4,  1, 12), ( 5,  1,  3))

# for u, v, w in connections:
#     graph2.add(u, v, w)

# print(graph2.min_expense())

# graph2.remove(3, 4)
# graph2.remove(1, 0)
# graph2.remove(4, 1)

# print(graph2.min_expense())

graph = Graph(40)
graph.add(25, 31, 21)
graph.add(35, 28, 15)
graph.add(0, 23, 74)
graph.add(3, 30, 45)
graph.add(18, 11, 22)
graph.add(15, 25, 99)
graph.add(16, 33, 90)
graph.add(6, 16, 30)
graph.add(27, 14, 42)
graph.add(12, 24, 86)
graph.add(14, 37, 83)
graph.add(12, 28, 36)
graph.add(19, 6, 69)
graph.add(0, 16, 37)
graph.add(19, 32, 25)
graph.add(30, 18, 36)
graph.add(1, 35, 39)
graph.add(31, 4, 28)
graph.add(33, 8, 51)
graph.add(31, 30, 29)
graph.add(22, 33, 64)
graph.add(28, 5, 28)
graph.add(26, 30, 44)
graph.add(8, 15, 24)
graph.add(30, 28, 99)
graph.add(25, 18, 30)
graph.add(5, 33, 23)
graph.add(13, 3, 67)
graph.add(0, 33, 55)
graph.add(33, 1, 52)
graph.add(35, 15, 11)
graph.add(18, 16, 76)
graph.add(28, 8, 83)
graph.add(26, 30, 68)
graph.add(21, 24, 73)
graph.add(7, 15, 95)
graph.add(27, 36, 13)
graph.add(17, 6, 56)
graph.add(15, 20, 99)
graph.add(11, 22, 78)
graph.add(38, 18, 79)
graph.add(38, 20, 29)
graph.add(4, 1, 79)
graph.add(26, 7, 12)
graph.add(3, 21, 67)
graph.add(16, 37, 42)
graph.add(34, 4, 82)
graph.add(1, 28, 88)
graph.add(32, 33, 38)
graph.add(34, 32, 28)
graph.add(23, 8, 77)
graph.add(17, 5, 96)
graph.add(13, 24, 32)
graph.add(10, 11, 56)
graph.add(36, 6, 80)
graph.add(2, 39, 56)
graph.add(0, 37, 67)
graph.add(24, 13, 24)
graph.add(14, 12, 78)
graph.add(12, 10, 69)
print(graph.min_expense())
#>>> 1460
graph.remove(29, 27)
graph.remove(5, 24)
graph.remove(7, 14)
graph.remove(0, 37)
graph.remove(0, 37)
graph.remove(0, 37)
graph.remove(32, 33)
graph.remove(32, 33)
graph.remove(32, 33)
graph.remove(6, 16)
graph.remove(6, 16)
graph.remove(6, 16)
graph.remove(16, 37)
graph.remove(16, 37)
graph.remove(16, 37)
graph.remove(31, 30)
graph.remove(31, 30)
graph.remove(31, 30)
graph.remove(13, 3)
graph.remove(13, 3)
graph.remove(13, 3)
graph.remove(22, 37)
graph.remove(38, 20)
graph.remove(38, 20)
graph.remove(38, 20)
graph.remove(23, 28)
graph.remove(5, 33)
graph.remove(5, 33)
graph.remove(5, 33)
graph.remove(16, 25)
graph.remove(33, 17)
graph.remove(12, 10)
graph.remove(12, 10)
graph.remove(12, 10)
graph.remove(12, 24)
graph.remove(12, 24)
graph.remove(12, 24)
graph.remove(11, 8)
graph.remove(9, 15)
graph.remove(24, 4)
print(graph.min_expense())
#1700