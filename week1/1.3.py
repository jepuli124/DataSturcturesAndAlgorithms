def triangle(a, b, c):
    if a < 0 or b < 0 or c < 0:
        return False
    
    if(a >= b+c):
        return False
    if(b >= a+c):
        return False
    if(c >= b+a):
        return False
    
    return True
     

print(triangle(3, 5, 4))    # True
print(triangle(-1, 2, 3))   # False
print(triangle(5, 9, 14))   # False
print(triangle(30, 12, 29)) # True