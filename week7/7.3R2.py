def queen(n, m):
    if n == m:
        board = [None] * n
        counter = [0]

        search(board, n, m, 0, counter)
        return counter[0]
    boards = firstLevel(n, m)
    boards = mainLoop(boards, n, m)
    return len(boards)

def search(board, n, m, y, counter):
    if m == y:
        found = 0
        for x in board:
            if x != None:
                found += 1
        #print(board)
        if found == m:
            counter[0] += 1
    else:
        for x in range(n):
            if can_be_placed(board, y, x):
                board[y] = x
                search(board.copy(), n, m, y + 1, counter)



def can_be_placed(list, y, x):
    for queenPos in range(len(list)):
        if x == list[queenPos]:
            return False
        if list[queenPos] != None:
            if (x + y - list[queenPos] - queenPos ) == 0 or (x - list[queenPos]) == (y - queenPos):
                return False
    return True


def mainLoop(boards, n, m):
    for queens in range((m-1)):
        boards2 = []
        
        for trueBoard in boards:
            for places in range((trueBoard[-1][0])*n, (n*n)):
                board = trueBoard.copy()
                xPos = places // (n)
                yPos = places % (n)
                if yPos+(m-(queens)-3) > n :
                    continue
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

def firstLevel(n, m):
    boards = []
    for places in range(n*(n+1//2)):
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

# 4 4
# 10 10
# 10 7
# 9 2
# 8 2
# 10 5
# 7 7
# 7 6
#