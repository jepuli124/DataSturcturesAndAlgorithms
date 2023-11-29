def pairs(s):
    cursor = 0
    calculator = 0
    location = []
    while True:
        if s[cursor] == "1":
            location.append(cursor)
        if cursor >= len(s)-1:
            break
        cursor += 1 
    print("amount of 1: " +str(len(location)))    
    print("last 1: " + str(location[-1] ))
    for x in range(len(location)-1):
        calculator += location[-1] - x - location[0]
        print("Calculator is now Before:" + str(calculator))
    for x in range(len(location)-1):    
        calculator += (x)*(len(location)-1-x)
        print("Calculator is now After:" + str(calculator))

    return calculator    


print(pairs("100101"))          # 10
print(pairs("101"))             # 2
print(pairs("100100111001"))    # 71

#1 1 = 1*1 = 1
#1 1 1 = 1*2, 2*1 = 4
#1 1 1 1 = 1*3, 2*2, 3*1 = 10 
#1 1 1 1 1 = 1*4, 2*3, 3*2, 4*1 = 20
#1 1 1 1 1 1 = 1*5, 2*4, 3*3, 4*2, 5*1 = 35

