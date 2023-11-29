def sums(items):
    sumList = []
    sumList.append(items[0])
    sumTrue = []
    for x in range(len(items)):
        if x == 0:
            sumTrue.append(True)
        else:
            sumTrue.append(False)
    returnList = []

    allTrue = False
    while not allTrue:
        result = sum(sumList)
        if result not in returnList:
            returnList.append(result)
        sumList = []
        carry = False
        allTrue = True
        for x in range(len(sumTrue)):
            if carry == True and sumTrue[x] == False:
                sumTrue[x] = True
                sumTrue[x-1] = False
                carry = False
                allTrue = False
            elif carry == True and sumTrue[x] == True:
                sumTrue[x-1] = False
            elif sumTrue[x] == True:
                carry = True
            else:
                allTrue = False
            if x+1 == len(sumTrue) and sumTrue[x] == True:
                setValue = False
                for y in range(len(sumTrue)):
                    if sumTrue[y] == False and setValue == False:
                        sumTrue[y] = True
                        setValue = True
                    elif setValue == True:
                        sumTrue[y] = False
                break
    
        

    
    return len(returnList)

print(sums([1, 2, 3]))                  # 6
print(sums([2, 2, 3]))                  # 5
#print(sums([1, 3, 5, 1, 3, 5]))         # 18
#print(sums([1, 15, 5, 23, 100, 55, 2])) # 121