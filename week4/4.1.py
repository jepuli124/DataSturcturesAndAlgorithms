class HashLinear:
    fixedList = []
    len = 0
    def __init__(self, value):
        for x in range(value):
            self.fixedList.append("empty")
        self.len = value

    def hash(self, data):
        sum = 0
        for i in range(len(data)):
            sum += ord(data[i])
        return sum % self.len
    
    def insert(self, data):
        desiredSlot = self.hash(data)
        counter = desiredSlot
        while True:
            if self.fixedList[counter] == "empty" or self.fixedList[counter] == data:
                self.fixedList[counter] = data
                break
            else:
                counter += 1
                if counter >= self.len:
                    counter = 0
            if counter == desiredSlot:
                break

    def print(self):
        for x in self.fixedList:
            if x != "empty":
                print(x, end=" ")
        print("")

    def delete(self, data):
        desiredSlot = self.hash(data)
        counter = desiredSlot
        while True:
            if self.fixedList[counter] == data:
                self.fixedList[counter] = "empty"
                break
            else:
                counter += 1
                if counter >= self.len:
                    counter = 0
            if counter == desiredSlot:
                break




table = HashLinear(8)
table.insert("BM40A1500")
table.insert("fOo")
table.insert("123")
table.insert("Bar1")
table.insert("10aaaa1")
table.insert("BM40A1500")
table.print()   # 10aaaa1 BM40A1500 fOo 123 Bar1
table.delete("fOo")
table.delete("Some arbitary string which is not in the table")
table.delete("123")
table.print()   # 10aaaa1 BM40A1500 Bar1