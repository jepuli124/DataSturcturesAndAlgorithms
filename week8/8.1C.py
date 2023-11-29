def jumps(n, a, b):
    matchCounter = 0
    amountOfa = 0
    amountOfb = 0
    choices = []
    while True:
        while (amountOfa*a)+(amountOfb*b) < n:
            amountOfa += 1
        if (amountOfa*a)+(amountOfb*b) == n:
            if (amountOfa, amountOfb) not in choices:
                choices.append((amountOfa, amountOfb))
        amountOfa = 0
        amountOfb += 1
        if (amountOfa*a)+(amountOfb*b) == n:
            if (amountOfa, amountOfb) not in choices:
                choices.append((amountOfa, amountOfb))
        elif (amountOfb*b) > n:
            break
    for x in choices:
        matchCounter += (factorial(x[0]+x[1]))//(factorial(x[0])*factorial(x[1]))
    return matchCounter

def factorial(n): #https://www.geeksforgeeks.org/factorial-in-python/
    returnvalue = 1
    for x in range(n):
        returnvalue *= (x+1)
    return returnvalue




print(jumps(4, 1, 2)) # 5
print(jumps(8, 2, 3)) # 4
print(jumps(11, 6, 7)) # 0
print(jumps(30, 3, 5)) # 58
print(jumps(100, 4, 5)) # 1167937

print(jumps(10000, 8, 94)) 
print(jumps(10000, 38, 98)) 
print(jumps(10000, 56, 125)) 