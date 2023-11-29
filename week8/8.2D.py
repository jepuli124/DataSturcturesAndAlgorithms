def sums(items):
    sums = set()
    
    possibleList = []
    for x in range(len(items)):
        sums.add(items[x])
        possibleList.append(False)
    breakValue = 1
    while breakValue:
        breakValue = 0
        sumValue = 0
        for x in range(len(possibleList)):
            if possibleList[-x-1] == False:
                breakValue = 1
                possibleList[-x-1] = True
                
                for y in range(len(possibleList)):
                    if possibleList[y] == True:
                        sumValue += items[y]
                sums.add(sumValue)
                break
            if possibleList[-x-1] == True:
                possibleList[-x-1] = False
    return len(sums)


print(sums([1, 2, 3]))                  # 6
print(sums([2, 2, 3]))                  # 5
print(sums([1, 3, 5, 1, 3, 5]))         # 18
print(sums([1, 15, 5, 23, 100, 55, 2])) # 121