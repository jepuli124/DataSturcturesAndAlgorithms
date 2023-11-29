def jumps(n, a, b):
    listOfViable = []
    counter = -1
    matchCounter = 0
    while len(listOfViable) != 0 or counter == -1:
        testlist = []
        if counter != -1:
            testlist = listOfViable[0].copy()
        testlist.append(a)
        if sum(testlist) == n:
            matchCounter += 1

        elif sum(testlist) < n:
            listOfViable.append(testlist)
        if counter != -1:
            testlist = listOfViable.pop(0)
        else:
            testlist = []
        testlist.append(b)
        if sum(testlist) == n:
            matchCounter += 1
        elif sum(testlist) < n:
            listOfViable.append(testlist)
        counter += 1
        

    return matchCounter



print(jumps(4, 1, 2)) # 5
print(jumps(8, 2, 3)) # 4
print(jumps(11, 6, 7)) # 0
print(jumps(30, 3, 5)) # 58
print(jumps(100, 4, 5)) # 1167937