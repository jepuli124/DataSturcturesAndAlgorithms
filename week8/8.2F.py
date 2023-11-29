def sums(items):
    sums = set() 
    for x in items:
        sums.add(x)
    sumAllways = [None] * len(items)
    while None in sumAllways:
        sumValue = []
        for xx in sumAllways:
            if xx != None:
                sumValue.append(xx)
        changeNumber = -1
        counter = 0
        summa = 0
        for y in range(len(sumAllways)):
            if len(sumValue)!= 0 and sumAllways[y] != None:
                summa = sum(sumValue)+items[y]
                sums.add(summa)
            elif changeNumber == -1:
                changeNumber = counter
            counter += 1
        if changeNumber == -1:
            break
        for z in range(changeNumber-1):
            sumAllways[z] = None
        sumAllways[changeNumber] = items[changeNumber]

        
    print(sums)

    return len(sums)


print(sums([1, 2, 3]))                  # 6
print(sums([2, 2, 3]))                  # 5
print(sums([1, 3, 5, 1, 3, 5]))         # 18
print(sums([1, 15, 5, 23, 100, 55, 2])) # 121