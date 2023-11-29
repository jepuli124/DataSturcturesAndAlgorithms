def jumps(n, a, b):
    listOfViable = []
    matchCounter = 0
    possibleList = []

    for x in range(n//b):
        possibleList.append(b)
    breakValue = 1
    listOfViable.append(possibleList.copy())
    while breakValue:
        breakValue = 0
        for x in range(len(possibleList)):
            if possibleList[-x-1] == b:
                breakValue = 1
                possibleList[-x-1] = a
                listOfViable.append(possibleList.copy())
                break
            if possibleList[-x-1] == a:
                possibleList[-x-1] = b


    while len(listOfViable) != 0:
        if sum(listOfViable[0]) == n:
            matchCounter += 1
            listOfViable.pop(0)
            continue
        testlist = listOfViable[0].copy()
        testlist.append(a)
        if sum(testlist) == n:

            matchCounter += 1
        elif sum(testlist) < n:
            listOfViable.append(testlist)
        testlist = listOfViable.pop(0)
        testlist.append(b)
        if sum(testlist) == n:

            matchCounter += 1
        elif sum(testlist) < n:
            listOfViable.append(testlist)
    
    return matchCounter


print(jumps(4, 1, 2)) # 5
print(jumps(8, 2, 3)) # 4
print(jumps(11, 6, 7)) # 0
print(jumps(30, 3, 5)) # 58
print(jumps(100, 4, 5)) # 1167937