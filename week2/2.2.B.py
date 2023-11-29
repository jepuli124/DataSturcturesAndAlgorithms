def pairs(s):
    cursor = 0
    calculator = 0
    amountOfOne = 0
    amountFromLastOne = 1
    Sum = 0
    while True:
        if s[cursor] == "1":
            amountOfOne += 1
            cursor += 1 
            break   
        cursor += 1      
    while True:
        if s[cursor] == "1":
            amountOfOne += 1
            Sum += amountFromLastOne*(amountOfOne-1)
            calculator += Sum
            amountFromLastOne = 1
        else:
            amountFromLastOne += 1
        if cursor >= len(s)-1:
            break
        cursor += 1 


    return calculator    


print(pairs("100101"))          # 10
print(pairs("101"))             # 2
print(pairs("10010011100100"))    # 71
print(pairs("0010010011100111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"))