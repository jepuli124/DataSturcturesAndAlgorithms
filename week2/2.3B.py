def split(T):
    min = 1001
    max = 0
    secondMax = 0
    listOfBreakValues = []
    for x in T:
        if x > max:  
            if secondMax != 0 and not secondMax in listOfBreakValues:
                listOfBreakValues.append(secondMax)    
            max = x
            min = x
        if x > secondMax and secondMax != max:
            secondMax = x   
        if min >= x:
            counter = 0
            for y in range(len(listOfBreakValues)):
                #print(y, listOfBreakValues)
                if listOfBreakValues[-y-1] >= x:
                    counter += 1 
                else:
                    break   
            min = x
            for z in range(counter):
                listOfBreakValues.pop(-1)

    #print(listOfBreakValues)
    print(len(listOfBreakValues), end=" ")
    return len(listOfBreakValues)


#print(split([1, 6, 4, 1, 2, 2, 2, 6, 6, 13, 12, 7, 10, 19, 15, 17, 17, 17, 19, 18, 2, 32, 0 3,3 ,4, 12, 5, 6, 7, 8, 12, 9, 0, 6, 4, 32, 32, 3, 4, 43, 35, 55, 56, 67,64, 64, 43, 45, 34, 75 ,78]))

split([3, 3, 3, 3, 1, 8, 6, 5, 7, 8, 12, 11, 7, 11 ,8]) #returns 1.

split([1, 1, 2, 6, 1, 5, 7, 7, 7, 9, 9, 10, 13, 16, 12, 16, 11, 13]) #returns 2.

split([1, 6, 4, 1, 2, 2, 2, 6, 6, 13, 12, 7, 10, 19, 15, 17, 17, 17, 19, 18]) #returns 1.

split([1, 2, 3, 4, 4, 6, 5, 7, 9, 8, 7, 8]) #returns 5.

split([2, 1, 3, 4, 5]) #returns 2.

split([5, 4, 3, 2, 1]) #returns 1.

split([1, 2, 3, 4, 5, 6]) #returns 0.

split([6, 5, 4, 3, 2, 1]) #returns 1.

split([1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) #returns 5.

split([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) #returns 1.

split([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) #returns 0.

split([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11]) #returns 1.

split([11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) #returns 1.

split([1, 3, 5, 7, 9, 2, 4, 6, 8, 10, 11]) #returns 6.

split([11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 12]) #returns 1.

split([12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) #returns 1.

split([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) #returns 0.

split([12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 13]) #returns 1.

split([13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

split([1, 3, 5, 7, 9, 11, 2, 4, 6, 8, 10, 12, 13]) #returns 7.

#print(split([1,2,3,4,5]))       # 4
#print(split([5,4,3,2,1]))       # 0
#print(split([2,1,2,5,7,6,9]))   # 3
#print(split([1,2,3,1]))         # 0
#print(split([3, 3, 3, 3, 1, 8, 6, 5, 7, 8, 12, 11, 7, 11, 8]))  # 1
#print(split([1, 1, 2, 6, 1, 5, 7, 7, 7, 9, 9, 10, 13, 16, 12, 16, 11, 13])) # 4
#print(split([1, 6, 4, 1, 2, 2, 2, 6, 6, 13, 12, 7, 10, 19, 15, 17, 17, 17, 19, 18])) # 2
#print(split([1, 2, 3, 4, 4, 6, 5, 7, 9, 8, 7, 8])) # 5
