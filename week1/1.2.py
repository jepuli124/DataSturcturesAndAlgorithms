def primes(N):
    result = []
    for x in range(2,N+1):
        isPrime = True
        for y in range(2, x):
            if x % y == 0:
                isPrime = False
                break
        if isPrime:
            result.append(x)
    return len(result)       

        

print(primes(7))    # 4
print(primes(15))   # 6
print(primes(50))   # 15