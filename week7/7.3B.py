def queen(n, m):
    if m > n:
        return 0
    
    if n%2 != 0 or True:
        boards = firstLevel(n)
        boards = mainLoop(boards, n, m)
    else:
        boards = firstLevel2(n)
        boards = mainLoop2(boards, n, m)
        return boards
    # for board in boards:
    #     printBoard(board, n)
    return len(boards)

def mainLoop(boards, n, m):
    for queens in range((m-1)):
        boards2 = []
        
        for trueBoard in boards:
            for places in range((queens+1)*n, (n*n)):
                board = trueBoard.copy()
                xPos = places // (n)
                yPos = places % (n)
                continueValue = 0
                for queenPos in range(len(board)):
                    if xPos == board[queenPos][0]:
                        continueValue = 1
                        break
                    if yPos == board[queenPos][1]:
                        continueValue = 1
                        break
                    if (xPos + yPos - board[queenPos][0] - board[queenPos][1] ) == 0 or (xPos - board[queenPos][0]) == (yPos - board[queenPos][1]):
                        continueValue = 1
                        break   
                if continueValue == 1:
                    continue

                board.insert(xPos,(xPos, yPos))
                board = sortListByDuble(board)

                if board not in boards2:
                    boards2.append(board)
                    
        boards = boards2.copy()
    return boards

def mainLoop2(boards, n, m):
    for queens in range(((m)//2)-1):
        boards2 = []
        
        for trueBoard in boards:
            for places in range(((n//2)*n)):
                board = trueBoard.copy()
                
                xPos = places % (n//2)
                yPos = places // (n//2)
                continueValue = 0
                for queenPos in range(len(board)):
                    if xPos == board[queenPos][0]:
                        continueValue = 1
                        break
                    if yPos == board[queenPos][1]:
                        continueValue = 1
                        break

                    if (xPos + yPos - board[queenPos][0] - board[queenPos][1] ) == 0 or (xPos - board[queenPos][0]) == (yPos - board[queenPos][1]):
                        continueValue = 1
                        break   
                if continueValue == 1:
                    continue

                board.insert(xPos,(xPos, yPos))
                board = sortListByDuble(board)

                if board not in boards2:
                    boards2.append(board)
        #for x in boards2:
        #    print(x)
                    
        boards = boards2.copy()
    returnBoards = 0
    print(len(boards))
    for trueBoard in boards:
        
        board = trueBoard.copy()
        for x in trueBoard:
            xPos = (n-1)-x[0]
            yPos = (n-1)-x[1]
            board.append((xPos, yPos))
        #print("trueBoard:", trueBoard, "board:", board)
        xValues = []
        yValues = []
        continueValue = 0
        for tuble in board:
            if tuble[0] not in xValues:
                xValues.append(tuble[0])
            else:
                continueValue = 1
                #print("cutted in horizontal", board)
                break
            if tuble[1] not in yValues:
                yValues.append(tuble[1])
            else:
                continueValue = 1
                #print("cutted in vertical", board)
                break
            for x in range(0, len(xValues)-1):
                if (xValues[x] + yValues[x] - tuble[0] - tuble[1] ) == 0 or (xValues[x] - tuble[0]) == (yValues[x] - tuble[1]):
                    continueValue = 1
                    #print("cutted in diagonal", board, "x value", xValues[x], "y value", yValues[x], "tuble", tuble)
                    break  
            if continueValue == 1:
                break
        if continueValue == 0:
            returnBoards += 1 

    return returnBoards

def firstLevel(n):
    boards = []
    for places in range(n*n):
        xPos = places //(n)
        yPos = places % (n)
        board = []
        board.append((xPos, yPos))
        boards.append(board)
    return boards

def firstLevel2(n):
    boards = []
    for places in range((n//2)*n):
        xPos = places % (n//2)
        yPos = places // (n//2)
        board = []
        board.append((xPos, yPos))
        boards.append(board)
    return boards

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

def printBoard2(board, n):
    xd = ["0"] * (n//2)
    lol = []
    for i in range(n//2):
        lol.append(xd.copy())
    print(board)
    for queen in board:
        lol[queen[0]][queen[1]] = "X"
    for line in lol:
        print(line)
    print()

print("queen 4 4 ", queen(4, 4))  # 2
# print("queen 4 2 ", queen(4, 2))  # 44
# print("queen 6 4 ", queen(6, 4))  # 982
# print("queen 7 2 ", queen(7, 2))  # 700
print("queen 8 8 ", queen(8, 8))  # 92
# print(queen(3,3))
# print(queen(5,5))
# print(queen(7,7))
# print(queen(9,9))
