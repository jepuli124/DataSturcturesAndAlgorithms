class Board():
    listOfQueens = []
    listOfFreeSlots = []

    def __init__(self, n):
        for places in range(n*n):
            xPos = places //(n)
            yPos = places % (n)
            self.listOfFreeSlots.append((xPos, yPos))
    
    def setValues(self, listOfQueens, listOfFreeSlots):
        self.listOfQueens = listOfQueens
        self.listOfFreeSlots = listOfFreeSlots

    def getListOfQueen(self):
        return self.listOfQueens
    
    def getListOfFreeSlots(self):
        return self.listOfFreeSlots


    def addFirstQueen(self, xPos, yPos):
        self.listOfQueens.append((xPos, yPos))
        self.reduceFreeSlots(xPos, yPos)

    def addQueen(self, xPos, yPos):

        if len(self.listOfQueens) == 0:
            self.addFirstQueen(xPos, yPos)
            return True
        for queenPos in range(len(self.listOfFreeSlots)):
            if xPos == self.listOfFreeSlots[queenPos][0]:
                return False
            if yPos == self.listOfFreeSlots[queenPos][1]:
                return False
            if (xPos + yPos - self.listOfFreeSlots[queenPos][0] - self.listOfFreeSlots[queenPos][1] ) == 0 or (xPos - self.listOfFreeSlots[queenPos][0]) == (yPos - self.listOfFreeSlots[queenPos][1]):
                return False   

        self.listOfQueens.insert(xPos,(xPos, yPos))
        self.sortListByDuble()
        self.reduceFreeSlots(xPos, yPos)

        return True

    def copy(self):
        board = Board(0)
        board.setValues(self.getListOfQueen(), self.getListOfFreeSlots())
        return board

    def reduceFreeSlots(self, xPos, yPos):
        
        counter = 0
        for queenPos in range(len(self.listOfFreeSlots)):
            if xPos == self.listOfFreeSlots[queenPos-counter][0]:
                self.listOfFreeSlots.pop(queenPos-counter)
                counter += 1
        counter = 0
        for queenPos in range(len(self.listOfFreeSlots)):
            if yPos == self.listOfFreeSlots[queenPos-counter][1]:
                self.listOfFreeSlots.pop(queenPos-counter)
                counter += 1

        counter = 0
        for queenPos in range(len(self.listOfFreeSlots)):
            if (xPos + yPos - self.listOfFreeSlots[queenPos-counter][0] - self.listOfFreeSlots[queenPos-counter][1] ) == 0 or (xPos - self.listOfFreeSlots[queenPos-counter][0]) == (yPos - self.listOfFreeSlots[queenPos-counter][1]):
                self.listOfFreeSlots.pop(queenPos-counter)
                counter += 1
        
    
    def sortListByDuble(self):
        for i in range(1, len(self.listOfQueens)):
            j = i-1
            while (j >= 0) and (self.listOfQueens[j][0] > self.listOfQueens[j+1][0]):
                S1 = self.listOfQueens[j]
                S2 = self.listOfQueens[j+1]
                self.listOfQueens[j] = S2
                self.listOfQueens[j+1] = S1
                j -= 1


def queen(n, m):
    boards = firstLevel(n)
    boards2 = boards.copy()

    if m > n:
        return 0
    
    for queens in range((m-1)):
        boards2 = []
        
        for trueBoard in boards:
            for places in range((queens+1)*n, (n*n)):
                board = trueBoard.copy()
                xPos = places // (n)
                yPos = places % (n)
                board.addQueen(xPos, yPos)

                if board not in boards2:
                    boards2.append(board)
                    
        boards = boards2.copy()
    return len(boards)


def firstLevel(n):
    boards = []
    for places in range(n*n):
        xPos = places //(n)
        yPos = places % (n)
        board = Board(n)
        board.addQueen(xPos, yPos)
        boards.append(board)
    return boards



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