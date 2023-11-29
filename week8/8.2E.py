def sums(items):
    sums = set()
    sum = set()
    for x in items:
        sum.add(x)
        for y in sums:
            sum.add(x+y)
        sums.update(sum)
    #print(sums)
    return len(sums)






print(sums([1, 2, 3]))                  # 6
print(sums([2, 2, 3]))                  # 5
print(sums([1, 3, 5, 1, 3, 5]))         # 18
print(sums([1, 15, 5, 23, 100, 55, 2])) # 121