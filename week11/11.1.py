class route:
    def __init__(self):
        self.length = 0
        self.path = [0]
    
    def append(self, vertex, length):
        self.path.append(vertex)
        self.length += length


def salesman(city_map):
    bound = [float('inf')]
    averageLength = 0
    counter = 1
    for x in city_map:
        for y in x:
            if y != 0:
                averageLength += y
                counter += 1
    averageLength /= counter  
    path = pathRecursiveSearch(city_map, route(), bound, averageLength)
    return path.path

def pathRecursiveSearch(city_map, path, bound, averageLength):
    if len(city_map) == len(path.path):
        path.append(0, city_map[path.path[-1]][0]) #TODO
        cost = path.length
        if cost < bound[0]:
            bound[0] = cost
            newPath = route()
            newPath.length = path.length
            newPath.path = path.path
            return newPath
        return
    paths = []
    for IterationNumber, pathsToOtherCities in enumerate(city_map):
        if IterationNumber in path.path:
            for OtherCity, lengthToOtherCity in enumerate(pathsToOtherCities):
                if lengthToOtherCity + path.length + averageLength*(len(city_map)-len(path.path)) < bound[0] and OtherCity not in path.path:
                    newPath = route()
                    newPath.length = path.length
                    newPath.path = path.path
                    newPath.append(OtherCity, lengthToOtherCity) #TODO
                    #print(newPath)
                    returnPath = pathRecursiveSearch(city_map, newPath, bound, averageLength)
                    if returnPath: paths.append(returnPath)
    shortestPath = None
    shortestPathLength = float('inf')

    for possiblePath in paths:
        cost = possiblePath.length
        print(cost)
        if cost < shortestPathLength:
            shortestPath = possiblePath
            shortestPathLength = cost

    return shortestPath
        


    
cost = 0

city_map = [
    #     0   1   2   3   4
        [ 0, 12, 19, 16, 29],   # 0
        [12,  0, 27, 25,  5],   # 1
        [19, 27,  0,  8,  4],   # 2
        [16, 25,  8,  0, 14],   # 3
        [29,  5,  4, 14,  0]    # 4
        ]

path = salesman(city_map)
for i in range(len(city_map)):
    cost += city_map[path[i]][path[i+1]]

print(path)     # [0, 1, 4, 2, 3, 0]
print(cost)     # 45