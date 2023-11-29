class MinHeap:
    def __init__(self, list):
        self.list = list
        self.sort()
        
    def push(self, value):
        self.list.append(value)
        self.sort()

    def pop(self):
        returnvalue = self.list[0]
        self.list[0] = 10000000
        self.sort()
        self.list.pop(len(self.list)-1)
        return returnvalue


    def print(self):
        for x in self.list:
            print(x, end=" ")
        print("")

    def sort(self):
        #for x in range(len(self.list)-1):
        #    print(self.list)
        #    if self.list[-x-1] < self.list[((len(self.list)-x)//2)-1]:
        #        big = self.list[((len(self.list)-x)//2)-1]
        #        self.list[((len(self.list)-x)//2-1)] = self.list[-x-1]
        #        self.list[-x-1] = big
        #FirstNonLeafNode = ((len(self.list))//2)-1
        while True:
            moved = 0
            for x in range(((len(self.list))//2)-1, -1, -1):
                node = self.list[x]
                if len(self.list)-1 >= x*2 + 2: 
                    if node > self.list[x*2+1] or node > self.list[x*2 + 2]:
                        moved = 1
                        if self.list[x*2+1] < self.list[x*2 + 2]:
                            self.list[x] = self.list[x*2+1]
                            self.list[x*2+1] = node
                        else:
                            self.list[x] = self.list[x*2+2]
                            self.list[x*2+2] = node
                elif len(self.list)-1 >= x*2 + 1:
                    if node > self.list[x*2+1]:
                        moved = 1
                        self.list[x] = self.list[x*2+1]
                        self.list[x*2+1] = node
            if moved == 0:
                break







heap = MinHeap([4, 8, 6, 5, 1, 2, 3])
heap.print()        # 1 4 2 5 8 6 3 
print(heap.pop())   # 1
heap.push(9)
heap.print()        # 2 4 3 5 8 6 9