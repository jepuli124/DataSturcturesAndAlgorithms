def sums(items):
    sumList = []
    sumList.append(items[0])

    returnList = []
    for x in items:
        if x not in returnList:
            returnList.append(x)
    sumCounter = 1
    while True:
        counter = 0 + len(sumList)
        while counter < len(items):
            result = sum(sumList)+items[counter]
            if result not in returnList:
                returnList.append(result)
            counter += 1
        sumList.pop(len(sumList)-1)

        

        if sumCounter > len(items)-1:
            print(sumCounter, len(items))
            sumList.append(items[len(sumList)])
            sumCounter = 0 + len(sumList)-3
            sumList.append(items[sumCounter])
        else:
            sumList.append(items[sumCounter])
            sumCounter += 1
            
        print(sumList)
        if sumList == items:
            break

            

    print(returnList)
    return len(returnList)-1

print(sums([1, 2, 3]))                  # 6
print(sums([2, 2, 3]))                  # 5
#print(sums([1, 3, 5, 1, 3, 5]))         # 18
#print(sums([1, 15, 5, 23, 100, 55, 2])) # 121
