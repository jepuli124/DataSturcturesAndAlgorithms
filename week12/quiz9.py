def setUp(value):
    amount = [0, value]
    path = [1]
    recursive(amount, path)
    return amount[0]

def recursive(amount, path):
    if path[-1] > amount[1]:
            return
     
    if path[-1] == amount[1]:
        amount[0] += 1
        return
    newPath1 = path.copy()
    newPath2 = path.copy()
    newPath1.append(newPath1[-1]+1)
    newPath2.append(newPath2[-1]+2)
    recursive(amount, newPath1)
    recursive(amount, newPath2)
    return


print(setUp(20))