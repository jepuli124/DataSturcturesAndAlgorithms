def sales(cars, customers):
    cars.sort()
    customers.sort()
    count = 0
    for x in customers:
        if x >= cars[count]:
            count += 1
    return count

print(sales([20, 15, 12], [25, 15, 11]))                        # 3
print(sales([13, 7, 2, 3, 12, 4, 19], [3, 25, 16, 14]))         # 4
print(sales([24, 6, 20, 21, 12, 5], [25, 1, 24, 15]))           # 3
print(sales([14, 9, 10, 15, 18, 20], [24, 17, 9, 22, 12, 4]))   # 5