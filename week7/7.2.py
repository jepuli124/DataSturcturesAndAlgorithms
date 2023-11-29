def subsets(n: int) -> list:
    listOfLists = []
    listValues = []

    for x in range(n):
        listValues = []
        listValues.append(x+1)
        listOfLists.append(transferValues(listValues))
        while len(listValues) < x+1:
            listValues.insert(0, 1)
            listOfLists.append(transferValues(listValues))
            listValues[0] += 1
            while True:
                listValues, found = checkIfSameValue(listValues)
                if found == False:
                    break
            breakPoint = 0
            isBreak = False
            for z in listValues:
                if breakPoint == z:
                    isBreak = True
                else:
                    breakPoint = z
                   
            if isBreak:
                #print("isBreak", listValues)
                break
            elif listValues[-1] <= x+1:
                listOfLists.append(transferValues(listValues))
            else:
                break
        
    return listOfLists

def transferValues(listValues):
    transferList = []
    for x in listValues:
        transferList.append(x)
    return transferList

def checkIfSameValue(listValues):
    found = False
    for y in range(len(listValues)-1):
        if listValues[y] == listValues[y+1]: 
            listValues[y+1] += 1
            found = True
            listValues = transferValues(listValues[y+1:len(listValues)])
            break
    return listValues, found


print(subsets(1))   # [[1]]
print(subsets(2))   # [[1], [2], [1, 2]]
print(subsets(3))   # [[1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
print(subsets(4))   # [[1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3], [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]]
print(subsets(5))
S = subsets(10)
print(S[95])    # [6, 7]
print(S[254])   # [1, 2, 3, 4, 5, 6, 7, 8]
print(S[826])   # [1, 2, 4, 5, 6, 9, 10]
