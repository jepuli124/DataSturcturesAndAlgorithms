import random
def knapsack(items, K):
    table = [[""] * (K + 1) for _ in range(len(items))]
    table[0][0] = "O"           # OMIT
    table[0][items[0]] = "I"    # INCLUDE
    for i in range(1, len(items)):
        table[i][0] = "O"
        for k in range(1, K + 1):
            if k >= items[i] and table[i - 1][k - items[i]] != "":        
                table[i][k] += "I"
            if table[i - 1][k] != "":
                table[i][k] += "O"
    return table

def algorithm(L):
    k = 0
    for i in range(L):
        x = random.randint(0,1000)/1000
        y = random.randint(0,1000)/1000
        if x**2 + y**2 < 1: k = k + 1
    return 4 * k / L

#print(algorithm(10000))
for x in knapsack([5,2,3,7,1], 8):
    print(x)