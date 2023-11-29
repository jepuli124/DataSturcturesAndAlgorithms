class Node:
    def __init__(self, value):
        self.value = value
        self.NextR = None
        self.NextL = None

    def getValue(self):
        if self.value != None:
            return self.value
        else:
            return None

    def getNextR(self):
        if self.NextR != None:
            return self.NextR    
        else:
            return None   
        
    def getNextL(self):
        if self.NextL != None:
            return self.NextL    
        else:
            return None   
            
    def setValue(self, value):
        self.value = value
    def setNextR(self, node):
        self.NextR = node
    def setNextL(self, node):
        self.NextL = node    


class BST:
    def __init__(self):
        self.first = Node(None)
        self.mirrored = 1
    def insert(self, value):
        if self.first.getValue() == None:
            self.first.setValue(value)
            return
        pointer = self.first    
        while True:
            if pointer.getValue()*self.mirrored > value*self.mirrored:
                if pointer.getNextL() != None:
                    pointer = pointer.getNextL()
                else:
                    pointer.setNextL(Node(value))  
                    return  
            elif pointer.getValue()*self.mirrored < value*self.mirrored:
                if pointer.getNextR() != None:
                    pointer = pointer.getNextR()
                else:
                    pointer.setNextR(Node(value))  
                    return    
            else:
                return
    def search(self, value):
        if self.first.getValue() == None:
            return False
        pointer = self.first    
        while True:
            if pointer.getValue()*self.mirrored > value*self.mirrored:
                if pointer.getNextL() != None:
                    pointer = pointer.getNextL()
                else:
                    return False
            elif pointer.getValue()*self.mirrored < value*self.mirrored:
                if pointer.getNextR() != None:
                    pointer = pointer.getNextR()
                else:
                    return False
            else:
                return True

    def preorder(self):
        if self.first.getValue() == None:
            return 
        pointer = self.first
        self.preorderRecursive(pointer)
        print("")

    def preorderRecursive(self, pointer):
        print(pointer.getValue(), end=" ")
        if pointer.getNextL() != None:
            self.preorderRecursive(pointer.getNextL())
        if pointer.getNextR() != None:
            self.preorderRecursive(pointer.getNextR()) 

    def remove(self, value):
        mirroredHere = 0
        if self.mirrored == -1:
            mirroredHere = 1
            self.mirror()
        if self.first.getValue() == None:
            if mirroredHere == 1:
                self.mirror()
            return False
        elif self.first.getValue() == value:
            removable = self.first
            if removable.getNextL() == None and removable.getNextR() != None:
                self.first = removable.getNextR()
                if mirroredHere == 1:
                    self.mirror()
                return
            elif removable.getNextR() == None and removable.getNextL() != None:
                self.first = removable.getNextL()
                if mirroredHere == 1:
                    self.mirror()
                return
            elif removable.getNextR() == None and removable.getNextL() == None:
                self.first = None
                if mirroredHere == 1:
                    self.mirror()
                return
            leftHigh = self.first.getNextL()
            rightHigh = self.first.getNextR()
            if leftHigh != None:
                if leftHigh.getNextR() != None:
                    leftRightHigh = leftHigh.getNextR()
                    if rightHigh != None:
                        leftHigh.setNextR(rightHigh)
                        pointer2 = rightHigh
                        while pointer2.getNextL() != None:
                            pointer2 = pointer2.getNextL()
                        pointer2.setNextL(leftRightHigh)
                else:
                    leftHigh.setNextR(rightHigh)
            self.first = leftHigh
            if mirroredHere == 1:
                self.mirror()
            return

        pointer = self.first    
        LorR = None
        while True:
            if pointer.getValue() > value:
                if pointer.getNextL() != None:
                    if pointer.getNextL().getValue() == value:
                        LorR = "left"
                        break
                    else:
                        pointer = pointer.getNextL()
                else:
                    if mirroredHere == 1:
                        self.mirror()
                    return

            elif pointer.getValue() < value:
                if pointer.getNextR() != None:
                    if pointer.getNextR().getValue() == value:
                        LorR = "right"
                        break
                    else:
                        pointer = pointer.getNextR()
                else:
                    if mirroredHere == 1:
                        self.mirror()
                    return
            else:
                if mirroredHere == 1:
                    self.mirror()
                return "error"
        
        if LorR == "left":
            removable = pointer.getNextL()
            if removable.getNextL() == None and removable.getNextR() != None:
                pointer.setNextL(removable.getNextR())
                if mirroredHere == 1:
                    self.mirror()
                return
            elif removable.getNextR() == None and removable.getNextL() != None:
                pointer.setNextL(removable.getNextL())
                if mirroredHere == 1:
                    self.mirror()
                return
            elif removable.getNextR() == None and removable.getNextL() == None:
                pointer.setNextL(None)
                if mirroredHere == 1:
                    self.mirror()
                return
            leftHigh = removable.getNextL()
            rightHigh = removable.getNextR()
            if leftHigh.getNextR() != None:
                leftRightHigh = leftHigh.getNextR()
                leftHigh.setNextR(rightHigh)
                pointer2 = rightHigh
                while pointer2.getNextL() != None:
                    pointer2 = pointer2.getNextL()
                pointer2.setNextL(leftRightHigh)
            else:
                leftHigh.setNextR(rightHigh)
            pointer.setNextL(leftHigh)
            if mirroredHere == 1:
                self.mirror()
            return
        elif LorR == "right":
            removable = pointer.getNextR()
            if removable.getNextL() == None and removable.getNextR() != None:
                pointer.setNextR(removable.getNextR())
                if mirroredHere == 1:
                    self.mirror()
                return
            elif removable.getNextR() == None and removable.getNextL() != None:
                pointer.setNextR(removable.getNextL())
                if mirroredHere == 1:
                    self.mirror()
                return
            elif removable.getNextR() == None and removable.getNextL() == None:
                pointer.setNextR(None)
                if mirroredHere == 1:
                    self.mirror()
                return
            leftHigh = removable.getNextL()
            rightHigh = removable.getNextR()
            if leftHigh.getNextR() != None:
                leftRightHigh = leftHigh.getNextR()
                leftHigh.setNextR(rightHigh)
                pointer2 = rightHigh
                while pointer2.getNextL() != None:
                    pointer2 = pointer2.getNextL()
                pointer2.setNextL(leftRightHigh)
            else:
                leftHigh.setNextR(rightHigh)
            pointer.setNextR(leftHigh)
            if mirroredHere == 1:
                self.mirror()
            return
        if mirroredHere == 1:
            self.mirror()

    def postorder(self):
        if self.first.getValue() == None:
            return 
        pointer = self.first
        self.postorderRecursive(pointer)
        print("")
    
    def postorderRecursive(self, pointer):
        if pointer.getNextL() != None:
            self.postorderRecursive(pointer.getNextL())
        if pointer.getNextR() != None:
            self.postorderRecursive(pointer.getNextR())
        print(pointer.getValue(), end=" ") 

    def inorder(self):
        if self.first.getValue() == None:
            return 
        pointer = self.first
        self.inorderRecursive(pointer)
        print("")

    def inorderRecursive(self, pointer):
        if pointer.getNextL() != None:
            self.inorderRecursive(pointer.getNextL())
        print(pointer.getValue(), end=" ")
        if pointer.getNextR() != None:
            self.inorderRecursive(pointer.getNextR())
    
    def breadthfirst(self):
        if self.first.getValue() == None:
            return 
        else:
            print(self.first.getValue(), end=" ")
        pointer = self.first
        counter = 1
        success = 1
        while success != 0:
            listOfMoves = []
            success = 0
            for x in range(counter):
                listOfMoves.append("L")
            while True:
                noneReach = False
                pointer = self.first
                for x in listOfMoves:
                    if x == "L":
                        if pointer.getNextL() != None:
                            pointer = pointer.getNextL()
                        else:
                            noneReach = True
                            break
                    elif x == "R":
                        if pointer.getNextR() != None:
                            pointer = pointer.getNextR()
                        else:
                            noneReach = True
                            break
                if pointer.getValue() != None and not noneReach:
                    print(pointer.getValue(), end=" ")
                    success = 1
                if not "L" in listOfMoves:
                    break
                for x in range(len(listOfMoves)):
                    if listOfMoves[-x-1] == "L":
                        listOfMoves[-x-1] = "R"
                        break
                    elif listOfMoves[-x-1] == "R":
                        listOfMoves[-x-1] = "L"
            counter += 1
                

        #print(self.breadthfirstRecursive(pointer))
        print("")
    
    def mirror(self):
        if self.mirrored == -1:
            self.mirrored = 1
        else:
            self.mirrored = -1
        if self.first.getValue() == None:
            return 
        pointer = self.first
        self.mirrorRecursive(pointer)
        print("")
    
    def mirrorRecursive(self, pointer):
        if pointer.getNextL() == None and pointer.getNextR() != None:
            pointer.setNextL(pointer.getNextR())
            pointer.setNextR(None)
        elif pointer.getNextR() == None and pointer.getNextL() != None:
            pointer.setNextR(pointer.getNextL())
            pointer.setNextL(None)
        elif pointer.getNextR() != None and pointer.getNextL() != None:
            right = pointer.getNextR()
            pointer.setNextR(pointer.getNextL())
            pointer.setNextL(right)
            

        if pointer.getNextL() != None:
            self.mirrorRecursive(pointer.getNextL())
        if pointer.getNextR() != None:
            self.mirrorRecursive(pointer.getNextR())
        
    





#Tree = BST()
#keys = [5, 9, 1, 3, 7, 7, 4, 6, 2]

#for key in keys:
#    Tree.insert(key)

#Tree.preorder()         # 5 1 3 2 4 9 7 6

#print(Tree.search(6))   # True
#print(Tree.search(8))   # False

#Tree.remove(1)
#Tree.preorder()         # 5 3 2 4 9 7 6
#Tree.remove(9)
#Tree.preorder()         # 5 3 2 4 7 6 
#Tree.remove(3)
#Tree.preorder()         # 5 2 4 7 6


#tree = BST()

#for num in (14, 19, 13, 23, 12, 17, 16, 10, 15, 11, 22, 28, 30, 25, 20):
#    tree.insert(num)

#tree.postorder() # 11 10 12 13 15 16 17 20 22 25 30 28 23 19 14
#tree.inorder() # 10 11 12 13 14 15 16 17 19 20 22 23 25 28 30
#tree.breadthfirst() # 14 13 19 12 17 23 10 16 22 28 11 15 20 25 30



#Tree2 = BST()
#keys = [5, 9, 1, 3, 7, 7, 4, 6, 2]

#for key in keys:
#    Tree2.insert(key)
#Tree2.preorder()         # 5 1 3 2 4 9 7 6
#Tree2.postorder()        # 1 3 2 4 9 7 6 5
#Tree2.inorder()          # 1 2 3 4 5 6 7 9
#Tree2.breadthfirst()     # 5 1 9 3 7 2 4 6
Tree = BST()
keys = [5, 9, 1, 3, 7, 7, 4, 6, 2]

for key in keys:
    Tree.insert(key)

Tree.preorder()         # 5 1 3 2 4 9 7 6
Tree.mirror()
Tree.preorder()         # 5 9 7 6 1 3 4 2

Tree.insert(8)
Tree.remove(3)
print(Tree.search(2))   # True
Tree.preorder()         # 5 9 7 8 6 1 2 4
Tree.mirror()
Tree.preorder()         # 5 1 2 4 9 7 6 8
