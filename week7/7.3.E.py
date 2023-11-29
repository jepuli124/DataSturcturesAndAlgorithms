def queen(n, m):
    if m > n:
        return 0
    

    boards = firstLevel(n)
    boards = mainLoop(boards, n, m)

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

def firstLevel(n):
    boards = []
    for places in range(n*n):
        xPos = places //(n)
        yPos = places % (n)
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


print("queen 4 4 ", queen(4, 4))  # 2
print("queen 4 2 ", queen(4, 2))  # 44
print("queen 6 4 ", queen(6, 4))  # 982
print("queen 7 2 ", queen(7, 2))  # 700
print("queen 8 8 ", queen(8, 8))  # 92