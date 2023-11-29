def split(T):
    print("\n")
    high = 1001
    highest = 0
    low = 0
    lowest = 1001
    lowCounter = 0
    highCounter = 0
    lowCalculator = 0
    highCalculator = 0
    sameLow = 0 
    sameHigh = 0
    highValues = []
    lowValues = []
    state = 1
    if(len(T)% 2 == 0):
        midway = len(T)/2 -1
        even = True
    else:
        midway = (len(T))/2-0.5   
        even = False
    
    for x in range(len(T)):

        if state == 1 and even == False and x >= midway:
            print("State 2 by odd midway")
            state = 2

        if T[x] <= lowest and lowest != -1:
            if state == 2:
                lowest = -1
            else:    
                print("lowest: "+ str(T[x]) + " at: " + str(x))
                lowest = T[x]
            lowCalculator = 0
            lowValues.clear()  
            
        if T[x] >= low and state == 1:
            if(low == T[x]):
                sameLow += 1
            else:
                sameLow = 0
            if sameLow <= 1:         
                print("low: "+ str(T[x]) + " at: " + str(x))
                lowValues.append(T[x])
                low = T[x]
                lowCounter = x+1
                lowCalculator += 1
        if len(lowValues) > 0:        
            if T[x] < lowValues[0]:
                low = T[x]
                sameLow = 1
                print("removing low", T[x])
                lowValues.reverse()
                counter = 0
                for x in range(len(lowValues)):
                    if lowValues[x-counter] >= T[x]:
                        lowValues.pop(x-counter)
                        counter +=1
                        lowCalculator -= 1
                    else:
                        break
                lowValues.reverse()    

        if state == 1 and even == True and x >= midway:
            print("State 2 by even midway")
            state = 2  

        if T[(-1*x)-1] >= highest and highest != -1:
            if state == 2:
                highest == -1
            else:    
                print("highest: "+ str(T[(-1*x)-1]) + " at: " + str((-1*x)-1))
                highest = T[(-1*x)-1]
            highCalculator = 0
            highValues.clear()      
        if T[(-1*x)-1] <= high and state == 1:
            if(high == T[(-1*x)-1]):
                sameHigh += 1
            else:
                sameHigh = 0
            if sameHigh <= 1:
                print("high: "+ str(T[(-1*x)-1]) + " at: " + str((-1*x)-1))
                highValues.append(T[(-1*x)-1])
                high = T[(-1*x)-1]
                highCounter = len(T)-1-x
                highCalculator += 1
        if len(highValues) > 0:
            if T[(-1*x)-1] > highValues[0]:
                high = T[(-1*x)-1]
                sameHigh = 1
                print("removing high", T[(-1*x)-1])
                highValues.reverse()
                counter = 0
                for x in range(len(highValues)):
                    if highValues[x-counter] <= T[(-1*x)-1]:
                        highValues.pop(x-counter)
                        counter +=1
                        highCalculator -= 1
                    else:
                        break
                highValues.reverse()
           
        if state == 1 and high <= low:
            state = 2
            print("State 2 by high <= low")
        if highest == -1 and lowest == -1:
            print("No possible solutions")
            return 0    

    print("Listan pituus:" + str(len(T)))
    print("Low Counter:" + str(lowCounter))
    print("High Counter:" + str(highCounter))

    

    #for x in range(lowCounter):
    #    T[x]
    
    return lowCalculator+highCalculator        

print(split([1,2,3,4,5]))       # 4
print(split([5,4,3,2,1]))       # 0
print(split([2,1,2,5,7,6,9]))   # 3
print(split([1,2,3,1]))         # 0
print(split([3, 3, 3, 3, 1, 8, 6, 5, 7, 8, 12, 11, 7, 11, 8]))  # 1
print(split([1, 1, 2, 6, 1, 5, 7, 7, 7, 9, 9, 10, 13, 16, 12, 16, 11, 13])) # 4
print(split([1, 6, 4, 1, 2, 2, 2, 6, 6, 13, 12, 7, 10, 19, 15, 17, 17, 17, 19, 18])) # 2
print(split([1, 2, 3, 4, 4, 6, 5, 7, 9, 8, 7, 8])) # 5



# 1 2 3 4 5
#0 |     |
#1   | |
#2     
#3
# 1 2 3 4 5 6
#0 |       |
#1   |   |
#2     |
#3