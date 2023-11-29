def sums(items):
    sums = []
    #listOfViable = []
    possibleList = []
    for x in range(len(items)):
        possibleList.append(False)
    breakValue = 1
    #listOfViable.append(possibleList.copy())
    while breakValue:
        breakValue = 0
        
        sumValue = 0
        for x in range(len(possibleList)):
            
            if possibleList[-x-1] == False:
                
                breakValue = 1
                possibleList[-x-1] = True
                #sumList.append(items[-x-1])
                #print(possibleList)
                #listOfViable.append(possibleList.copy())
                #print(sumList)
                #sumValue += items[-x-1]
                sumValue = 0
                for y in range(len(possibleList)):
                    if possibleList[y] == True:
                        sumValue += items[y]


                if sumValue not in sums:
                    sums.append(sumValue)
                break
            if possibleList[-x-1] == True:
                #sumList.append(items[-x-1])
                #sumValue += items[-x-1]
                possibleList[-x-1] = False
    return len(sums)

print(sums([1, 2, 3]))                  # 6
print(sums([2, 2, 3]))                  # 5
print(sums([1, 3, 5, 1, 3, 5]))         # 18
print(sums([1, 15, 5, 23, 100, 55, 2])) # 121
        