def salesman(city_map):
    bound = [9000]
    return pathRecursiveSearch(city_map, [0], bound)

def pathRecursiveSearch(city_map, path, bound):
    cost = pathLength(path, city_map)

    if len(city_map) == len(path):
        path.append(0)
        costNew = pathLength(path, city_map)
        if costNew < bound[0]:
            bound[0] = costNew
            print(path, bound[0])
            return path.copy()
        return
    
    if cost >= bound[0]:
        return
    
    paths = []
    for otherCity in range(len(city_map)):
        if otherCity not in path:
            newPath = path.copy()
            newPath.append(otherCity)
            returnPath = pathRecursiveSearch(city_map, newPath, bound)
            if returnPath:
                paths.append(returnPath)

    shortestPath = None
    shortestPathLength = 10**6

    for possiblePath in paths:
        cost = pathLength(possiblePath, city_map)
        if cost < shortestPathLength:
            shortestPath = possiblePath
            shortestPathLength = cost
    
    return shortestPath

def pathLength(path, city_map):
    cost = 0
    for i in range(len(path)-1):
        cost += city_map[path[i]][path[i+1]]
    return cost
cost = 0
if __name__ == "__main__":
    
    cost = 0

    city_map = [
        [ 0, 12, 19, 16, 29],
        [12,  0, 27, 25,  5],
        [19, 27,  0,  8,  4],
        [16, 25,  8,  0, 14],
        [29,  5,  4, 14,  0]
        ]

    path = salesman(city_map)
    for i in range(len(city_map)):
        cost += city_map[path[i]][path[i+1]]
    
    print(path)     # [0, 1, 4, 2, 3, 0]
    print(cost)     # 45