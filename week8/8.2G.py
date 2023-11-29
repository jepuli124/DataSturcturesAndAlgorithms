def sums(items):

    sums = set()
    sumValueList = []
    for x in range(len(items)):
        sum = []
        sum.append(items[x])
        #print(sum)
        sumValueList = []
        for z in sums:
            sumValueList.append(z)
        for y in range(len(sumValueList)):
            sum.append(items[x]+sumValueList[y])
            #print(sum)
        sums.update(sum)
    #print(sums)
    return len(sums)






print(sums([1, 2, 3]))                  # 6
print(sums([2, 2, 3]))                  # 5
print(sums([1, 3, 5, 1, 3, 5]))         # 18
print(sums([1, 15, 5, 23, 100, 55, 2])) # 121