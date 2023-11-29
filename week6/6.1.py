
class AVLNode:
    def __init__(self, value):
        self.value = value
        self.NextR = None
        self.NextL = None
        self.balance = 0




class AVL:
    def __init__(self):
        self.first = AVLNode(None)
        self.isBalance = True
    
    def insert(self, key: int):
        self.first = self.insertRecursive(self.first, key)

    def insertRecursive(self, pointer, key):
        if pointer == None or pointer.value == None:
            pointer = AVLNode(key)
            self.is_balanced = False
        elif key < pointer.value:
            pointer.NextL = self.insertRecursive(pointer.NextL, key)
            if not self.is_balanced:                           
                if pointer.balance >= 0:
                    if pointer.balance == 1:      
                        self.is_balanced = True
                    pointer.balance -= 1
                else:                                      
                    if pointer.NextL.balance == -1:
                        pointer = self.RRotation(pointer)  
                    else:
                        pointer = self.LRRotation(pointer)   
                    self.is_balanced = True
        elif key > pointer.value:
            pointer.NextR = self.insertRecursive(pointer.NextR, key)
            if not self.is_balanced:                           
                if pointer.balance <= 0:
                    if pointer.balance == -1:      
                        self.is_balanced = True
                    pointer.balance += 1
                else:                                      
                    if pointer.NextR.balance == 1:
                        pointer = self.LRotation(pointer)  
                    else:
                        pointer = self.RLRotation(pointer)   
                    self.is_balanced = True
        return pointer
    
    def RRotation(self, pointer):
        nextL = pointer.NextL                   
        pointer.NextL = nextL.NextR             
        nextL.NextR = pointer
        nextL.balance = 0
        pointer.balance = 0
        return nextL
    def LRotation(self, pointer):
        nextR = pointer.NextR                   
        pointer.NextR = nextR.NextL             
        nextR.NextL = pointer
        nextR.balance = 0
        pointer.balance = 0
        return nextR

    def LRRotation(self, pointer):
        nextL = pointer.NextL
        NextLR = nextL.NextR
        if NextLR != None:
            nextL.NextR = NextLR.NextL
        else:
            nextL.NextR = None
        NextLR.NextL = nextL
        pointer.NextL = NextLR.NextR
        NextLR.NextR = pointer
        nextL.balance = 0
        pointer.balance = 0
        if NextLR.balance == -1:
            pointer.balance = 1
        elif NextLR.balance == 1:
            nextL.balance = -1
        else:
            nextL.balance = 0
            pointer.balance = 0
        NextLR.balance = 0
        return NextLR
    def RLRotation(self, pointer):
        nextR = pointer.NextR
        NextRL = nextR.NextL
        if NextRL != None:
            nextR.NextL = NextRL.NextR
        else:
            nextR.NextL = None
        NextRL.NextR = nextR
        pointer.NextR = NextRL.NextL
        NextRL.NextL = pointer
        nextR.balance = 0
        pointer.balance = 0
        if NextRL.balance == 1:
            pointer.balance = -1
        elif NextRL.balance == -1:
            nextR.balance = 1
        else:
            nextR.balance = 0
            pointer.balance = 0
        NextRL.balance = 0
        return NextRL

    def preorder(self):
        if self.first.value == None:
            return 
        pointer = self.first
        self.preorderRecursive(pointer)
        print("")

    def preorderRecursive(self, pointer):
        print(str(pointer.value) + ";" + str(pointer.balance), end=" ")
        if pointer.NextL != None:
            self.preorderRecursive(pointer.NextL)
        if pointer.NextR != None:
            self.preorderRecursive(pointer.NextR)
    
    def inorder(self):
        if self.first.value == None:
            return 
        pointer = self.first
        self.inorderRecursive(pointer)
        print("")

    def inorderRecursive(self, pointer):
        if pointer.NextL != None:
            self.inorderRecursive(pointer.NextL)
        print(pointer.value, end=" ")
        if pointer.NextR != None:
            self.inorderRecursive(pointer.NextR)


Tree = AVL()
for key in [9, 10, 11, 3, 2, 6, 4, 7, 5, 1]: # , 6, 4, 7, 5, 1
    Tree.insert(key)
    Tree.preorder()
    #Tree.inorder()
Tree.preorder()     # 9;-1 4;0 2;0 1;0 3;0 6;0 5;0 7;0 10;1 11;0


#          9  
#           
#          9
#           10
#        
#         10
#        9  11
#    
#         10 
#        9  11
#       3
#
#         10
#        3  11
#       2 9
#        
#          9 
#        3   10  
#       2  6   11
#         
#
#
#
#