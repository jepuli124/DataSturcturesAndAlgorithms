def queen(n, m):
    if m > n:
        return 0
    boards = firstLevel(n)
    boards = otherLevels(n, m, boards)
    #boards = check(boards)
    
                

                

    return len(boards)


def firstLevel(n):
    boards = []
    for places in range(n*n):
        xPos = places //(n)
        yPos = places % (n)
        board = []
        board.append((xPos, yPos))
        boards.append(board)
    return boards

def otherLevels(n, m, boards):
    for queens in range((m-1)):
        boards2 = []
        for trueBoard in boards:
            for places in range((queens+1)*n, (n*n)):
                board = trueBoard.copy()
                xPos = places // (n)
                yPos = places % (n)
                board.insert(xPos,(xPos, yPos))
                boards2.append(board)
                    
        boards = boards2.copy()
    return boards

def check(boards):
    boards2 = []
    for board in boards:
        continueValue = 0
        xValues = []
        yValues = []

        for queenPos in range(len(board)):

            if board[queenPos][0] in xValues:
                continueValue = 1
                break
            else:
                xValues.append(board[queenPos][0])

            if board[queenPos][1] in yValues:
                continueValue = 1
                break
            else:
                yValues.append(board[queenPos][1])
            for z in range(len(xValues)):
                if (xValues[z] + yValues[z] - board[queenPos][0] - board[queenPos][1] ) == 0 or (xValues[z] - board[queenPos][0]) == (yValues[z] - board[queenPos][1]):
                    continueValue = 1
                    break   
            if continueValue == 1:
                break
        if continueValue == 1:
            continue
        board = sortListByDuble(board)
        if board not in boards2:
            boards2.append(board)
    return boards2

def sortListByDuble(list):
    for i in range(1, len(list)):
        j = i-1
        while (j >= 0) and (list[j][0] > list[j+1][0]):
            S1 = list[j]
            S2 = list[j+1]
            list[j] = S2
            list[j+1] = S1

            j -= 1
    return list

def printBoard(board, n):
    xd = ["0"] * n
    lol = []
    for i in range(n):
        lol.append(xd.copy())
    print(board)
    for queen in board:
        lol[queen[0]][queen[1]] = "X"
    for line in lol:
        print(line)
    print()

print("queen 4 4 ", queen(4, 4))  # 2
print("queen 4 2 ", queen(4, 2))  # 44
print("queen 6 4 ", queen(6, 4))  # 982
print("queen 7 2 ", queen(7, 2))  # 700
print("queen 8 8 ", queen(8, 8))  # 92