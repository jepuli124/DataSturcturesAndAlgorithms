class Node:
    def __init__(self, value):
        self.value = value
        self.Next = None

    def getValue(self):
        if self.value != None:
            return self.value
        else:
            return None

    def getNext(self):
        if self.Next != None:
            return self.Next     
        else:
            return None   
    def setValue(self, value):
        self.value = value
    def setNext(self, node):
        self.Next = node

class LinkedList:

    def __init__(self):
        self.first = Node(None)
    

    def append(self, value):
        if self.first.getValue() == None:
            self.first = Node(value)
        else:
            if self.first.getNext() == None:
                self.first.setNext(Node(value))
                return
            pointer = Node(None)
            pointer = self.first.getNext()
            while True:
                if pointer.getNext() != None:
                    pointer = pointer.getNext()
                else:
                    pointer.setNext(Node(value))
                    break


    def insert(self, value, position):
        if self.first.getValue() == None:
            if position == 0:
                self.first = Node(value)
                return
        
        if position == 0:
            node = Node(value)
            node.setNext(self.first)
            self.first = node
            return
        
        pointer = Node(None)
        pointer = self.first
        counter = 1
        
        while True:
            if position == counter:
                variable = Node(None)
                if pointer.getNext() != None:
                    variable = pointer.getNext()
                else:
                    variable = None    
                pointer.setNext(Node(value))
                pointer = pointer.getNext()
                pointer.setNext(variable)
                return
            if pointer.getNext() != None:
                counter += 1
                pointer = pointer.getNext()
            else:
                return


    def print(self):
        if self.first.getValue() == None:
            return
        print(self.first.getValue(), "->", end=" ")
        pointer = Node(None)
        pointer = self.first.getNext()
        while True:
            if pointer.getNext() != None:
                print(pointer.getValue(), "->", end=" ")
                pointer = pointer.getNext()
            else:
                print(pointer.getValue())
                break

    def delete(self, position):
        if position == 0:
            node = self.first.getNext()
            self.first = node
            return
        
        pointer = Node(None)
        pointer = self.first
        counter = 1
        
        while True:
            if position == counter:
                variable = Node(None)
                if pointer.getNext() == None:
                    return None
                variable = pointer.getNext()
                if variable.getValue() != None:
                    returnValue = variable.getValue()
                else:
                    returnValue = None
                if variable.getNext() != None:
                    variable = variable.getNext()
                else:
                    variable = None    
                pointer.setNext(variable)
                return returnValue
            if pointer.getNext() != None:
                counter += 1
                pointer = pointer.getNext()
            else:
                return
    def index(self, value):
        
        pointer = Node(None)
        pointer = self.first
        counter = 0
        
        while True:
            if pointer.getValue() == value:
                return counter
            if pointer.getNext() != None:
                counter += 1
                pointer = pointer.getNext()
            else:
                return -1

    def swap(self, positionA, positionB):
        pointer = Node(None)
        pointer = self.first
        counter = 0
        
        if positionA < positionB:
            positionMin = positionA
            positionMax = positionB
        elif positionA == positionB:
            return
        else:
            positionMin = positionB
            positionMax = positionA     

        swap= Node(None)
        firstValue = 0
        while True:
            if positionMin == counter:
                swap = pointer
                firstValue = pointer.getValue()
            if positionMax == counter:
                swap.setValue(pointer.getValue())
                pointer.setValue(firstValue)
                return
            

            if pointer.getNext() != None:
                counter += 1
                pointer = pointer.getNext()
            else:
                return
    def isort(self):
        pointer = Node(None)
        pointer = self.first
        numbers = []
        while True:
            numbers.append(pointer.getValue())
            if pointer.getNext() != None:
                pointer = pointer.getNext()
            else:
                break
        numbers = self.sort(numbers);    
        counter = 0
        pointer = self.first
        while True:
            pointer.setValue(numbers[counter])
            counter += 1
            if pointer.getNext() != None:
                pointer = pointer.getNext()
            else:
                break
    def sort(self, A):
        for i in range(1, len(A)):
            j = i-1
            while (j >= 0) and (A[j] > A[j+1]):
                S1 = A[j]
                S2 = A[j+1]
                A[j] = S2
                A[j+1] = S1

                j -= 1    
        return A            


L = LinkedList()
for num in (3, 5, 2, 7, 8, 10, 6):
    L.append(num)
L.print()   # 3 -> 5 -> 2 -> 7 -> 8 -> 10 -> 6
L.isort()
L.print()   # 2 -> 3 -> 5 -> 6 -> 7 -> 8 -> 10
