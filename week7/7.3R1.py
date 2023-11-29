def queen(n, m):
    board = [None] * n
    counter = [0]
    if n == m: searchSameBoardSize(board, n, m, 0, counter)
    else: searchFirstLevel(board, n, m, 0, counter)
    return counter[0]
    
def searchFirstLevel(firstBoard, n, m, y, counter):
    for variable in range((n-m)+1):
        board = firstBoard.copy()
        for x in range(n):
            if can_be_placed(board, y + variable, x):
                board[y+variable] = x
                search(board.copy(), n, m, y + variable + 1, counter)

def search(ogBoard, n, m, y, counter):
    if m == y:
        found = 0
        for x in ogBoard:
            if x != None:
                found += 1
        #print(board)
        if found == m:
            counter[0] += 1
    elif y+1 <= n:
        for x in range(n):
            board = ogBoard.copy()
            
            if can_be_placed(board, y, x):
                search(board.copy(), n, m, y + 1, counter)
                board[y] = x
                search(board, n, m, y + 1, counter)
            else:
                search(board, n, m, y + 1, counter)

def searchSameBoardSize(board, n, m, y, counter):
    if m == y:
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




#print("queen 4 4 ", queen(4, 4))  # 2
print("queen 4 2 ", queen(4, 2))  # 44
print("queen 6 4 ", queen(6, 4))  # 982
print("queen 7 2 ", queen(7, 2))  # 700
#print("queen 8 8 ", queen(8, 8))  # 92

# 4 4
# 10 10
# 10 7
# 9 2
# 8 2
# 10 5
# 7 7
# 7 6
#