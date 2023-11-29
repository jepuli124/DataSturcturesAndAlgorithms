def changes(A):
    counter = 0
    skip = 0
    for x in range(1, len(A), 2):
        c = A[x]
        if skip == 1:
            skip -= 1
            if x < len(A)-1:    
                if c == A[x+1]:
                    if x < len(A)-2:
                        if c == A[x+2]:
                            skip = 1
                            A[x+1] = "R"
                        else:    
                            A[x] = "R"
                    else:    
                        A[x] = "R"                
                    counter += 1 
            continue
        if c == A[x-1]:
            A[x] = "R"
            counter += 1
        elif x < len(A)-1:    
            if c == A[x+1]:
                if x < len(A)-2:
                    if c == A[x+2]:
                        skip = 1
                        A[x+1] = "R"
                    else:    
                        A[x] = "R"
                else:    
                    A[x] = "R"                
                counter += 1    
    print(A)
    return counter  




print(changes([1, 1, 0, 2, 2,3,4,6,7,8,4,4,4,4,5,3,6,3,2,1,3,4,3,2,4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,4,5,6,6,6,6]))     # 2
print(changes([1, 2, 3, 4, 5]))     # 0
print(changes([1, 1, 1, 1, 1]))     # 2